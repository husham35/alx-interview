#!/usr/bin/python3
"""
Island perimeter computing module.
"""


def island_perimeter(grid):
    """
    Computes the perimeter of an island with no lakes.
    """
    if not isinstance(grid, list):
        return 0

    perimeter = 0
    rows = len(grid)
    
    for i in range(rows):
        columns = len(grid[i])
        for j in range(columns):
            if grid[i][j] == 1:  # check if it's a land cell
                # check top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                
                # check right
                if j == columns - 1 or grid[i][j+1] == 0:
                    perimeter += 1
                
                # check bottom
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                
                # check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1

    return perimeter
