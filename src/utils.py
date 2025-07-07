import sys
import os
import pandas as pd
import numpy as np

from src.exception import custom_exception
from src.logger import logging

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

import dill   # to create the Pikcal file


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)



    except Exception as e:
        custom_exception(e,sys)




# def evaluate_model(X_train, y_train, X_test, y_test, models):
#     try:
#         report = {}

#         for model_name, model in models.items():
#             model.fit(X_train, y_train)  # Train model

#             y_train_prediction = model.predict(X_train)
#             y_test_prediction = model.predict(X_test)

#             train_model_score = r2_score(y_train, y_train_prediction)
#             test_model_score = r2_score(y_test, y_test_prediction)

#             report[model_name] = test_model_score

#         return report   

            
#     except Exception as e:
#         raise custom_exception(e,sys)    


def evaluate_model(X_train,y_train,X_test,y_test,models,params):
    try:
        report={}
        for i in range(len(models)):
            
            model=list(models.values())[i]
            para=params[list(models.keys())[i]]
            
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)
            
            
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            
            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)
            
            train_model_score=r2_score(y_train, y_train_pred)
            test_model_score=r2_score(y_test, y_test_pred)
            
            report[list(models.keys())[i]]=test_model_score
     

        return report
    except Exception as e:
        raise custom_exception(e,sys)
    




def load_object(file_path):
    try:
        with open(file_path,"rb")as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise custom_exception(e,sys)    