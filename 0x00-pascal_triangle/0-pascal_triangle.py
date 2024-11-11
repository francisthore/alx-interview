#!/usr/bin/python3
"""
Module to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Parameters:
        n (int): Number of rows in Pascal's Triangle.

    Returns:
        list of lists: A list of lists, where each sublist represents
        a row in Pascal's Triangle.
                       Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row_n in range(1, n):
        current_row = [1]

        for col_n in range(1, row_n):
            value = triangle[row_n - 1][col_n - 1] + triangle[row_n - 1][col_n]
            current_row.append(value)

        current_row.append(1)
        triangle.append(current_row)

    return triangle
