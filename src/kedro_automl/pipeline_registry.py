"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from kedro_automl.pipelines import data_preparation, modeling

def register_pipelines() -> dict[str, Pipeline]:
    dp = data_preparation.create_pipeline()
    md = modeling.create_pipeline()
    return {
        "__default__": dp + md,        # domyślnie uruchamia oba potoki
        "data_preparation": dp,
        "modeling": md
    }
    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
