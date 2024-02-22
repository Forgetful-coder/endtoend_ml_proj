from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging
import sys

class TrainPipeline:
    def __init__(self):
        pass

    def train(self):
        try:
            logging.info('Start data ingestion')
            data_ingestion = DataIngestion()
            train_data,test_data = data_ingestion.initiate_data_ingestion()

            logging.info('data transformation')
            data_transformation = DataTransformation()
            train_data_arr,test_data_arr,_= data_transformation.initiate_data_transformation(train_data,test_data)

            logging.info('Train and get  the best model and model score')
            model_trainer = ModelTrainer()
            
            (model_trainer.initiate_model_trainer(train_arr=train_data_arr,test_arr=test_data_arr))

        except Exception as e:
            raise CustomException(e,sys)
            
