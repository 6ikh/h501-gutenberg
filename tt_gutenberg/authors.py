from .transform import DATA, get_data

def list_authors(by_languages=False, alias=False):
    df = get_data()

    if alias:
        df = df[df["author_alias"].notna()]

    if by_languages:
        df = df.sort_values("aliases_count", ascending=False)

    if alias:
        return df["author_alias"].tolist()
