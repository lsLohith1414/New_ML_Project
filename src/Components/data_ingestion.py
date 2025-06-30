import os 
from src.logger import logging
from src.exception import custom_exception
import sys
import pandas as pd

from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.Components.data_transformation import DataTransformation
from src.Components.data_transformation import DataTransformationConfig


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
    train_data,test_data =data_ingst.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)









# import os
# import sys
# import pandas as pd
# from dataclasses import dataclass
# from sklearn.model_selection import train_test_split

# from src.logger import logging
# from src.exception import custom_exception


# @dataclass
# class DataIngestionConfig:
#     train_data_path: str = os.path.join("artifacts", "train.csv")
#     test_data_path: str = os.path.join("artifacts", "test.csv")
#     raw_data_path: str = os.path.join("artifacts", "data.csv")


# class DataIngestion:
#     """
#     Handles the data ingestion process: reading raw data, saving it,
#     and performing a train-test split.
#     """

#     def __init__(self):
#         self.ingestion_config = DataIngestionConfig()

#     def initiate_data_ingestion(self):
#         """
#         Reads raw data from source, splits it into train and test sets,
#         and saves them to the specified paths.
#         """
#         logging.info("Entered the data ingestion component.")

#         try:
#             source_path = os.path.join("notebook", "data", "stud.csv")
#             if not os.path.exists(source_path):
#                 logging.error(f"Source file does not exist: {source_path}")
#                 raise FileNotFoundError(f"Missing file: {source_path}")

#             df = pd.read_csv(source_path)
#             logging.info("Successfully read the dataset into a DataFrame.")

#             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

#             df.to_csv(self.ingestion_config.raw_data_path, index=False)
#             logging.info(f"Raw data saved to: {self.ingestion_config.raw_data_path}")

#             logging.info("Initiating train-test split.")
#             train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

#             train_set.to_csv(self.ingestion_config.train_data_path, index=False)
#             test_set.to_csv(self.ingestion_config.test_data_path, index=False)

#             logging.info(f"Train set saved to: {self.ingestion_config.train_data_path}")
#             logging.info(f"Test set saved to: {self.ingestion_config.test_data_path}")
#             logging.info("Data ingestion process completed successfully.")

#             return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

#         except Exception as e:
#             logging.error("Exception occurred during data ingestion.", exc_info=True)
#             raise custom_exception(e, sys)


# if __name__ == "__main__":
#     data_ingest = DataIngestion()
#     data_ingest.initiate_data_ingestion()
