import argparse
import os
import warnings
import sys
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import xgboost as xgb

from  CALERA_LIBRARIES import * 
from features import *

import logging
logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def main(args):
    try:
        data_train_path = args.data_train_path
        name_experiment = args.name_experiment
        data_train = pd.read_csv(data_train_path)
        data_train["Fecha"] = pd.to_datetime(data_train["Fecha"])
        
    except Exception as e:
        logger.exception("Unable to load training & test CSV, check your path. Error: %s", e)

    
    mlflow.tracking.set_tracking_uri("file:///C:/Users/VoxivaAI/Desktop/workspace_gustavo/github/DengAI-Predicting-Disease-Spread")
    try:
        experiment_id_val = mlflow.get_experiment_by_name(name_experiment)
        experiment_id = experiment_id_val.experiment_id

    except Exception as e:
        print(e)
        logger.exception("Unable to get experiment in MlFlow, check your path. Error: %s", e)
        experiment_id = mlflow.create_experiment(name_experiment)

    execution_date = datetime.now().strftime("%Y%m%d%H%M")
    name_experiment = 'dengue_experiment{}'.format(execution_date)


    reg_alpha_sys =  0.2
    max_depth_sys = 4
    n_estimators_sys = 2000
    learning_rate = 0.02

    params = {
        'reg_alpha': reg_alpha_sys,
        'max_depth': max_depth_sys,
        'n_estimators': n_estimators_sys,
        'learning_rate': learning_rate,
        'objective': "count:poisson",
        'eval_metric':'rmsle',
        'modelo': "xgboost"
    }

    model = xgb.XGBRegressor(reg_alpha     = params["reg_alpha"],  
                            n_estimators  = params["n_estimators"], 
                            learning_rate = params["learning_rate"],
                            objective     = params["objective"],
                            eval_metric   = params["eval_metric"])

    print("training")
    date_max = data_train.Fecha.max()
    date_threshold = date_max -pd.DateOffset(weeks = 2)
    
    condition_train = data_train.Fecha <= date_threshold
    y_train, X_train = data_train[condition_train].Cantidad_sum.values, data_train.loc[condition_train, :]
    X_test = data_train.loc[~condition_train, :]


    with mlflow.start_run(experiment_id = experiment_id, nested = False, run_name = name_experiment):
        model.fit(X_train[cols_train], y_train)

        y_pred = model.predict(X_test[cols_train])
        X_test["CantidadPred"] = y_pred
        X_test["CantidadPred"] = X_test["CantidadPred"].apply(lambda x: 0.0 if x<0 else x)
                       

        for key, item in params.items():
            mlflow.log_param(key, item)
        
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        ftr, name_image = getFeatureImportance(model, X_train[cols_train], "autoservicio")
        mlflow.log_artifact(name_image, "model")

        ftr.to_csv("feature_importance.csv", index = False)
        mlflow.log_artifact("feature_importance.csv", "model")

        X_test[cols_predictions].to_csv("predictions_{}.csv".format(execution_date), index = False)
        mlflow.log_artifact("predictions_{}.csv".format(execution_date), "model")

        print("saving model")
        mlflow.sklearn.log_model(model, "model", serialization_format = mlflow.sklearn.SERIALIZATION_FORMAT_PICKLE)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_raw', required = True, help = "ruta del archivo del entrenamiento")
    parser.add_argument('--name_experiment', required = True, help = "nombre del experimento de mlflow")

    args = parser.parse_args() 
    main(args)


    """
    python train.py  --data_raw file_dengue.csv   --name_experiment Autoservicio_SKU
    """