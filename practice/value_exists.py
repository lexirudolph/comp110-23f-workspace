def value_exists(inp_dict: dict[str, int], val: int) -> bool:
    """Return true is val is in inp_dict."""
    exists: bool = False
    for i in inp_dict:
        if inp_dict[i] == val:
            exists = True
    return exists