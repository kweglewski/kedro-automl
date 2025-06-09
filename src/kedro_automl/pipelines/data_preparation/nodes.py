import pandas as pd

def load_and_clean(df: pd.DataFrame) -> pd.DataFrame:
    # Przykład: usunięcie duplikatów i braków
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def generate_datetime_features(df: pd.DataFrame) -> pd.DataFrame:
    df['year'] = pd.to_datetime(df['year'], format='%Y').dt.year
    # jeśli w CSV jest kolumna daty, dostosuj poniżej
    return df
