from kedro.pipeline import Pipeline, node
from .nodes import run_automl

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=run_automl,
            inputs="feateng_wages",
            outputs="best_model",
            name="automl_node"
        )
    ])
