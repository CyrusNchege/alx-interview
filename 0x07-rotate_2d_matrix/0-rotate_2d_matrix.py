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
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = temp


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
