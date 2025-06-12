"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.19.13
"""

from kedro.pipeline import Pipeline, node
from .nodes import predict_income

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=predict_income,
            inputs="feateng_wages",       # zdefiniowane w catalog.yml
            outputs="predictions",
            name="predict_node"
        )
    ])