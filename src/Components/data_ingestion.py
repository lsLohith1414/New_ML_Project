import os 
from src.logger import logging
from src.exception import custom_exception
import sys
import pandas as pd

from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join("Artifacts","train.csv")
    test_data_path : str = os.path.join("Artifacts","test.csv")
    raw_data_path : str = os.path.join("Artifacts","data.csv")





class DataIngestion: 

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method or component")    

        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("reading the dataset as Dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,header=True,index=False)

            logging.info("Train test split is initiated")

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,header = True,index =False)

            test_set.to_csv(self.ingestion_config.test_data_path,header = True,index =False)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise custom_exception(e,sys)



if __name__=="__main__":
    data_ingst = DataIngestion()
    data_ingst.initiate_data_ingestion()
