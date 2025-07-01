import os
import sys

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor


from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from src.exception import custom_exception
from src.logger import logging
from src.utils import save_object, evaluate_model

from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("Artifacts","model.pkl")
        

class ModelTrainer:
    def __init__(self):
        self.model_Trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        logging.info("Model Training Process is start")

        try:
            logging.info("split training and test input data ")

            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],   # all columns except last (features)
                train_array[:, -1],    # last column (label)
                test_array[:, :-1],    # same for test
                test_array[:, -1]
            )


            models ={
                "Random Forest" : RandomForestRegressor(),
                "DecisionTree" : DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regressor": LinearRegression(),
                "K-Neighbors Regressor" : KNeighborsRegressor(),
                "XGB Regressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(),
                "AdBoosting Regressor": AdaBoostRegressor()
            }
            
            model_report:dict = evaluate_model(X_train=X_train,y_train = y_train , X_test = X_test, y_test = y_test , models = models)

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise custom_exception("No best model Found",sys)
            
            logging.info("Best found model on both test and training dataset")

            save_object(
                file_path=self.model_Trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)

            r2_scores = r2_score(y_test,predicted)

            return (
                best_model_name,
                r2_scores
            )
        

             
        except Exception as e :
            raise custom_exception(e,sys)
        