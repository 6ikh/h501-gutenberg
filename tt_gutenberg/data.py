import pandas as pd

def load_gutenberg_data():
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    return pd.read_csv(url)


def load_gutenberg_metadata():
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
    return pd.read_csv(url)
