from .data import load_gutenberg_data


def get_data():
    df_authors, df_metadata = load_gutenberg_data()

    df_authors = (
        df_authors
        .drop(columns=["author"], errors="ignore")
        .rename(columns={"alias": "author_alias"})
    )

    df = df_metadata.merge(
        df_authors,
        on="gutenberg_author_id",
        how="left"
    )

    df["translation_count"] = df.groupby(
        "gutenberg_author_id"
    )["language"].transform("nunique")

    return df


DATA = get_data()
