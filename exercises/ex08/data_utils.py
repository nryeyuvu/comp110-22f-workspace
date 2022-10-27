"""Dictionary related utility functions."""

__author__ = "730552319"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row_oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces table with the first 'n' rows of data for each column."""
    if len(table) <= n:
        return table
    modified: dict[str, list[str]] = {}
    for i in table:
        filler: list[str] = []
        for j in range(0, n):
            filler.append(table[i][j])
        modified[i] = filler
    return modified


def select(column: dict[str, list[str]], copy: list[str]) -> dict[str, list[str]]:
    """Produces table with specific subset of the original columns."""
    build_up: dict[str, list[str]] = {}
    for i in copy:
        build_up[i] = column[i]
    return build_up


def concat(column: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines the columns of two tables."""
    random: dict[str, list[str]] = {}
    for i in column:
        random[i] = column[i]
    for j in second:
        if j in random:
            for k in second[j]:
                random[j].append(k)
        else:
            random[j] = second[j]
    return random


def count(inputted_list: list[str]) -> dict[str, int]:
    """From a list of strings, determines the occurrence of each element in list."""
    freq_dict: dict[str, int] = {}
    for i in inputted_list:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict