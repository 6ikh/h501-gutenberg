# import get_data function from transform.py
from .transform import get_data

# function list_authors with parameters by_languages and alias set to false
# dont sort authors by languages and dont filter authors by alias
def list_authors(by_languages=False, alias=False):
    """
    Lists authors from the dataset

    Parameters:
    by_languages returns authors sorted by the number of unique languages
    alias filters the authors to include only those with an alias

    Returns:
    A list of author names or a Series of authors sorted by language counts
    """
    # Get the data from the transform module
    df = get_data()
    # Filter authors with alias if alias is True
    if alias:
        # Filter the DataFrame to include only rows where 'author_alias' is not null
        df = df[df["author_alias"].notna()]
    # If by_languages is True, group by author_alias and count unique languages
    if by_languages:
        # Group by author_alias, count the number of unique languages
        counts = df.groupby("author_alias")["language"].nunique()
        # Sort the counts in descending order
        df = counts.sort_values(ascending=False)
    # Return the list of authors or the DataFrame based on the alias parameter
    if alias:
        return df.index.tolist()
    # return the DataFrame with counts
    return df
