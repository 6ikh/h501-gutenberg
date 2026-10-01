from .transform import DATA

def list_authors(by_languages=False, alias=False):
    df = DATA

    if alias:
        df = df[df["alias"].notna()]

    if by_languages:
        df = df.sort_values("aliases_count", ascending=False)

    if alias:
        return df["alias"].tolist()
