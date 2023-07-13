import os,sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion

if __name__=='__main__':
    data_ingestion_obj=DataIngestion()
    train_path,test_path=data_ingestion_obj.initiateDataIngestion()
    print(train_path,test_path)
