import pickle
import pandas as pd
from pycaret.regression import load_model, predict_model

def predict_income(raw_new_data):
    """
    Wczytuje wytrenowany model z pliku i odpala predykcję
    z automatycznym preprocessingiem.
    """
    # 1) Załaduj model (ścieżka bez .pkl)
    model = load_model("data/07_model_output/best_model")
    # 2) Zrób predykcję – DataFrame z kolumną 'Label'
    result = predict_model(model, data=raw_new_data)
    return result