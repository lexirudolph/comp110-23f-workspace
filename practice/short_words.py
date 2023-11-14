def short_words(inp_list: list[str]) -> list[str]:
    """Filter out the shorter words."""
    ret_list = []
    for x in inp_list:
        if len(x) < 5:
            ret_list.append(x)
        else:
            print(f"{x} is too long!")
    return ret_list