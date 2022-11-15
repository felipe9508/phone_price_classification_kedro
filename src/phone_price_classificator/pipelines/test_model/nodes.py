"""
This is a boilerplate pipeline 'test_model'
generated using Kedro 0.18.3
"""
import logging
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import mlflow

logger = logging.getLogger(__name__)


def evaluate_model(model: DecisionTreeClassifier,  data: pd.DataFrame) -> str:

    X = data.drop('price_range', axis=1)
    y = data['price_range']

    k_fold = model_selection.KFold(n_splits=10)
    scoring = 'accuracy'
    score = (model_selection.cross_val_score(
        model, X, y.values.ravel(),  scoring=scoring, cv=k_fold))

    print(f"({score.mean()}, {score.std()})")
    mlflow.set_experiment('Clasificación del precio de los celulares')
    mlflow.log_metric("Validación cruzada media", score.mean())
    mlflow.log_metric("Desviación estandar", score.std())

    return f"Validación cruzada\n Promedio: {score.mean()} Desviación Estandar: {score.std()}"
