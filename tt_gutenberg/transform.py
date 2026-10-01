from .data import load_gutenberg_data, load_gutenberg_metadata


def get_data():
    authors = load_gutenberg_data()
    metadata = load_gutenberg_metadata()

    translation_count = (
        metadata.groupby("gutenberg_author_id")["language"]
        .nunique()
        .reset_index(name="translation_count")
    )

    df = authors.merge(translation_count, on="gutenberg_author_id", how="left")
    df["author_alias"] = df["alias"]

    return df
