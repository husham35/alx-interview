#!/usr/bin/python3
"""
A module to Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix in 90 degrees clockwise.
    Args:
        matrix (list): 2D square
    Returns:
        None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
