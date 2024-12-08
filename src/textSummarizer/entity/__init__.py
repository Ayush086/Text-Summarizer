from dataclasses import dataclass
from pathlib import Path

# decorator ensures that it's umimmutable (once created then it can't be changed/modified)
@dataclass(frozen=True)
class DataIngestionConfig:
    """Data ingestion configuration class."""
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    """Data Validation configuration class."""
    root_dir: Path          # root directory where validation is performed
    STATUS_FILE: str        # path to the file where validation status will be written
    ALL_REQUIRED_FILES: list  # list of required files to check for existence



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path

