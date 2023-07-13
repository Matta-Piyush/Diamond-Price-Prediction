import os,sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:

    def __init__(self) -> None:
        self.data_ingestion_config=DataIngestionConfig()
    
    def initiateDataIngestion(self):
        logging.info("Data Ingestion method starts")

        try:
            # Reading data
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Data has been read as pandas dataframe')

            train_part,test_part=train_test_split(df,test_size=0.3,random_state=10)
            logging.info('Data has been divided into two parts train and test')
            
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False)
            logging.info("Raw data is created")

            train_part.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            test_part.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            logging.info('Train and Test dataframe has been created')
            logging.info('Data Ingestion process completed')

            return (self.data_ingestion_config.train_data_path,self.data_ingestion_config.test_data_path)
        
        except Exception as e:
            logging.info("Exception occured at data ingestion stage")
            raise CustomException(e,sys)

