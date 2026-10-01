from .data import load_gutenberg_data, load_gutenberg_metadata


def get_data():
    authors = load_gutenberg_data()
    metadata = load_gutenberg_metadata()

    authors["author_alias"] = authors["alias"]

    return metadata.merge(
        authors,
        on="gutenberg_author_id",
        how="left"
    )


DATA = get_data()

