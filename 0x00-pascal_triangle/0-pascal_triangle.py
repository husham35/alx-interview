#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    that represents a pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    # creates a row and fills first and last index with 1
    for i in range(n):
        row = [0] * (i+1)
        row[0] = 1
        row[len(row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(row):
                x = pascal_triangle[i - 1][j]
                y = pascal_triangle[i - 1][j - 1]
                row[j] = x + y

        pascal_triangle[i] = row

    return pascal_triangle
