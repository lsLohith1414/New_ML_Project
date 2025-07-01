import sys 
import os
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from dataclasses import dataclass

from src.logger import logging
from src.exception import custom_exception

from src.utils import save_object



@dataclass
class DataTransformationConfig:
    """This class we create for if we want to give any type of input paths and input for the Data transformation component we use data_transformation_config"""
    preprocessor_pkl_object_path = os.path.join("Artifacts","preprocessor.pkl")



class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()


    def get_data_transformar_object(self):
        """This function is responsiable for data Transformation """
        try:
            numerical_columns = ["writing_score","reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",             
                "parental_level_of_education",    
                "lunch",                   
                "test_preparation_course"
            ]

            num_pipline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )



            cat_pipline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Numerical columns {numerical_columns}")
            logging.info(f"Categorical columns {categorical_columns}")


            preprosessor = ColumnTransformer(
                [
                    ("num_pipline",num_pipline,numerical_columns),
                    ("cat_pipline",cat_pipline,categorical_columns)
                ]
            )

            return preprosessor

        except Exception as e:
            raise custom_exception(e,sys)
        




    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df  = pd.read_csv(test_path)

            logging.info("Read Train and Test data is completed")

            logging.info("obtaining preprocessing object")

            preprocessor_obj =self.get_data_transformar_object()


            target_column_name = "math_score"

            numerical_columns = ["writing_score","reading_score"]


            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]


            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]
            

            logging.info("Applying preprocessof object on train dataframe and test dataframe")

            input_feature_train_arr =preprocessor_obj.fit_transform(input_feature_train_df)

            input_feature_test_arr =preprocessor_obj.transform(input_feature_test_df)


            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]

            logging.info("Saving preprocessing obj")

            save_object(
                file_path = self.data_transformation_config.preprocessor_pkl_object_path,
                obj = preprocessor_obj

            )


            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_pkl_object_path
            )

            

        except Exception as e:
            raise custom_exception(e,sys)
            

