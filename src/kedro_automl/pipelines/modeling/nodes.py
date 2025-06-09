import os
import pickle
from pycaret.regression import setup, compare_models

def run_automl(feateng_wages):
    # Inicjalizacja eksperymentu (bez interaktywnych pytań)
    exp = setup(
        data=feateng_wages,
        target='realrinc',
        verbose=False     # wycisza większość logów
    )
    best = compare_models()
    # Ręczne zapisanie modelu przez pickle
    output_dir = "data/07_model_output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "best_model.pkl"), "wb") as f:
        pickle.dump(best, f)
    return best
