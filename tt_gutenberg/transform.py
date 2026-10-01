import pandas as pd
from .data import load_gutenberg_data

def get_data():
    df = load_gutenberg_data()

    df["translation_count"] = df["alias"].str.count(",") + 1

    df["author_alias"] = df["alias"]

    if "language" not in df.columns:
        df["language"] = "unknown"

    return df


DATA = get_data()