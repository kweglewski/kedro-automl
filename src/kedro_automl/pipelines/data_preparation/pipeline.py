from kedro.pipeline import pipeline, node
from .nodes import load_and_clean, generate_datetime_features

def create_pipeline(**kwargs):
    return pipeline([
        node(func=load_and_clean,
             inputs="gss_wages",
             outputs="cleaned_wages",
             name="clean_wages_node"),
        node(func=generate_datetime_features,
             inputs="cleaned_wages",
             outputs="feateng_wages",
             name="feature_engineering_node"),
    ])
