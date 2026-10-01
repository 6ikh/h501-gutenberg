from .transform import DATA

def list_authors(by_languages=False, alias=False):
    df = DATA

    if by_languages:
        df = df.sort_values("translation_count", ascending=False)

    if alias:
        df = df[df["author_alias"].notna()]
        return df["author_alias"].drop_duplicates().tolist()

    return df
