#!/usr/bin/python3
"""Module to perform matrix operations"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n matrix 90 degrees clockwise in-place.
    """
    rotated = zip(*matrix[::-1])
    for i in range(len(matrix)):
        matrix[i] = list(rotated[i])


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)
