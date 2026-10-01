from .data import load_gutenberg_data


def list_authors(by_languages=False, alias=False):
    df = load_gutenberg_data()

    if alias:
        df = df[df["alias"].notna()]

    if by_languages:
        df["aliases_count"] = df["aliases"].str.count(",") + 1
        df = df.sort_values("translation_count", ascending=False)

    if alias:
        return df["alias"].tolist()
