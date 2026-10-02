# import necessary pandas
import pandas as pd

#function to load the data from the URLs
def load_gutenberg_data():
    """
    Loads Gutenberg authors and metadata from specified CSV URLs.

    Returns:
        A tuple containing two DataFrames, one for authors and one for metadata
    """
    # URLs for the authors and metadata CSV files
    authors_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    metadata_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
    # Load the CSV files into pandas DataFrames
    df_authors = pd.read_csv(authors_url)
    df_metadata = pd.read_csv(metadata_url)
    # Return the DataFrames
    return df_authors, df_metadata
