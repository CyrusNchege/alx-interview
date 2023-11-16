#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise.

Args:
    matrix (list[list[int]]): The 2D matrix to rotate.

Returns:
    None
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list[list[int]]): The 2D matrix to rotate.

    Returns:
        None
    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last, offset = layer, n - 1 - layer, 0
        for i in range(first, last):
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
            offset += 1
