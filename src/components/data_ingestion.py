# To read the data from the database or live stream

import os
import sys
from src.exception import CustomExceptions
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

# To create class variables.
from dataclasses import dataclass

 
 
@dataclass
 # class to save inputs
class DataIngestionConfig:
    # Define class variable
    train_data_path: str=os.path.join('artifacts', "train.csv") #Outputs are stored in the artifacts
    test_data_path: str=os.path.join('artifacts', "test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
       
    
    # create  my function  
    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion or component")
        try:
            pass
        except:
            pass
    

