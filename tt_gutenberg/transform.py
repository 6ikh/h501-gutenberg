import pandas as pd
from .data import load_gutenberg_data


def get_data():
    df = load_gutenberg_data()

    df["translation_count"] = df["aliases"].str.count("/") + 1
    df["author_alias"] = df["alias"]

    return df


DATA = get_data()
