"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""
from phone_price_classificator.pipelines.data_processing.nodes import get_data_from_url, process_data
from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=get_data_from_url,
             inputs="parameters",
             outputs="data_raw",
             name="read_data"),
        node(func=process_data,
             inputs="data_raw",
             outputs="data_clean",
             name="process_data")
    ])
