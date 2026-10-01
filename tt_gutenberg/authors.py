from .transform import get_data


def list_authors(by_languages=False, alias=False):
    df = get_data()

    if alias:
        df = df[df["author_alias"].notna()]

    if by_languages:
        counts = df.groupby("author_alias")["language"].nunique()
        df = counts.sort_values(ascending=False)

    if alias:
        return df.index.tolist()

    return df
