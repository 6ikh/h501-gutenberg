import pandas as pd


def load_gutenberg_data():
    authors_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    metadata_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"

    df_authors = pd.read_csv(authors_url)
    df_metadata = pd.read_csv(metadata_url)

    return df_authors, df_metadata
