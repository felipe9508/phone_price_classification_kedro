"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.3
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import mlflow
import mlflow.sklearn


def train_model(data: pd.DataFrame):
    X = data.drop('price_range', axis=1)
    y = data['price_range']

    model = DecisionTreeClassifier()

    mlflow.set_experiment('Clasificación del precio de los celulares')
    mlflow.set_tag("mlflow.runName", model.__class__.__name__)

    model.fit(X, y.values.ravel())
    return model
