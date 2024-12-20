from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_transformation import DataTranformation
from src.textSummarizer.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTranformation(config=data_transformation_config)
        data_transformation.convert()
