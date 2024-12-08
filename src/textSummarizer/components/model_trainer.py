from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch
from src.textSummarizer.entity import ModelTrainerConfig


# defining component
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt) # load tokenizer
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device) # load model
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus) # used to handle batches
        
        #loading data
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        
        # setting up model parameters
        # trainer_args = TrainingArguments(
        #     output_dir=self.config.root_dir, num_train_epochs = self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
        #     per_device_train_batch_size= self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_eval_batch_size,
        #     weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
        #     evaluation_strategy=self.config.evaluation_strategy, eval_steps=self.config.eval_steps, save_steps=self.config.save_steps,
        #     gradient_accumulation_steps=self.config.gradient_accumulation_steps
        # )
        
        # another approach
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
        )
        
        trainer = Trainer(model=model_pegasus, args=trainer_args,
                          tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                          train_dataset=dataset_samsum_pt["test"], # it must be train instead of test but the CPU is not responsding that's why testing data is used
                          eval_dataset=dataset_samsum_pt["validation"]
                        )
        
        trainer.train()
        
        ## save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegauses-samsum-model"))
        ## save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "pegauses-tokenizer"))