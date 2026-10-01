from .transform import get_data


def list_authors(by_languages=False, alias=False):
    df = get_data()

    if by_languages:
        df = df.sort_values("translation_count", ascending=False)

    if alias:
        df = df[df["author_alias"].notna()]
        return df["author_alias"].tolist()

    return df

