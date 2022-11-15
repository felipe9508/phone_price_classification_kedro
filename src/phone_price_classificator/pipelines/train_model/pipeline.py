"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.3
"""
from phone_price_classificator.pipelines.train_model.nodes import train_model
from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=train_model,
             inputs="data_clean",
             outputs="model_trained",
             name="train_model")
    ])
