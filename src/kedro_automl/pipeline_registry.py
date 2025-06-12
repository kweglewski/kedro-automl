"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from kedro_automl.pipelines import data_preparation, modeling, predict

def register_pipelines() -> dict[str, Pipeline]:
    dp = data_preparation.create_pipeline()
    md = modeling.create_pipeline()
    pr = predict.create_pipeline()
    
    return {
        "__default__": dp + md,        # domyślnie uruchamia oba potoki
        "predict": dp + md + pr,    # przygotowanie, model + predykcja
        "data_preparation": dp,
        "modeling": md,
        "predict_only": pr
    }
    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
