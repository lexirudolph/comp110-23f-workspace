"""Dictionary related utility functions."""

__author__ = "730416818"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows represented as dict[str, str]."""
    output: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        output.append(row)
    file_handle.close()
    return output


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Product a list of all values in a single column whose name is the second parameter."""
    output: list[str] = []
    for row in table:
        output.append(row[header])
    return output


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represented as a dictionary of columns."""
    output = {}
    column_names = table[0].keys()
    for header in column_names:
        column_values = [row[header] for row in table]
        output[header] = column_values
    return output


def head(inp_dict: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first n rows of data for each column."""
    if not inp_dict:
        return {}
    output = {}
    column_names = inp_dict.keys()
    for header in column_names:
        new_list = []    
        for i in inp_dict[header][:n]:
            new_list.append(i)
            output[header] = new_list
    return output


def select(inp_dict: dict[str, list[str]], inp_list: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    output = {}
    for i in inp_list:
        output[i] = inp_dict[i]
    return output


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    output = {}
    for column_name in table_1.keys():
        output[column_name] = table_1[column_name]
    for column_name in table_2.keys():
        if column_name in output:
            output[column_name] += table_2[column_name]
        else:
            output[column_name] = table_2[column_name]
    return output


def count(inp_list: list[str]) -> dict[str, int]:
    """Produce a dictionary from a given list where each key is a unique value in the given list and each value associated is the count of the number of times where that value appeared in the input list."""
    output = {}
    for i in inp_list:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1
    return output