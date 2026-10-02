# import load_gutenberg_data function from data.py
from .data import load_gutenberg_data

# function get_data()
def get_data():
    """
    Retrieves and merges author data with metadata from the Gutenberg dataset.

    This function loads author information and metadata, then merges them
    based on the 'gutenberg_author_id'. It returns a DataFrame containing
    the combined data.

    Returns:
        DataFrame: A merged DataFrame containing metadata and author details.
    """
    # Load authors and metadata using the load_gutenberg_data function
    authors, metadata = load_gutenberg_data()
    # Create a new author_alias column from the existing alias column
    authors["author_alias"] = authors["alias"]
    # Merge authors & metadata dfs on 'gutenberg_author_id' using a left join
    return metadata.merge(
        authors,
        on="gutenberg_author_id",
        how="left"
    )

# Initialize DATA variable to hold the merged dataset
DATA = get_data()
