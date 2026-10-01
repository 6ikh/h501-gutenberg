from .transform import DATA

def list_authors(by_languages=False, alias=False):
    df = DATA

    if alias:
        df = df[df["author_alias"].notna()]
        df = df.sort_values("aliases_count", ascending=False)

    if by_languages and not alias:
        df = df.sort_values("aliases_count", ascending=False)

    if alias:
        return df["author_alias"].tolist()

    return df
