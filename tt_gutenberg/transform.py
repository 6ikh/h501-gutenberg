import pandas as pd
from .data import load_gutenberg_data

def get_data():
    df = load_gutenberg_data()

    df["aliases_count"] = df["alias"].str.count(",") + 1
    return df

DATA = get_data()