from .data import load_gutenberg_data


def get_data():
    authors, metadata = load_gutenberg_data()

    authors["author_alias"] = authors["alias"]

    return metadata.merge(
        authors,
        on="gutenberg_author_id",
        how="left"
    )


DATA = get_data()
