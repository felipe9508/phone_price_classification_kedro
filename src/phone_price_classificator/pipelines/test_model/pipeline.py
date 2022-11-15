"""
This is a boilerplate pipeline 'test_model'
generated using Kedro 0.18.3
"""
from phone_price_classificator.pipelines.test_model.nodes import evaluate_model
from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=evaluate_model,
            inputs=["model_trained",
                    "data_clean"],
            outputs="cross_validation_score",
            name="model_evaluation"
        )
    ])
