#!/usr/bin/python3
"""
A module to find N queens solution.
"""
import sys


# solutions = []  # the list of possible solutions

# n = 0  # the size of the chessboard

# pos = None  # the list of possible positions on chessboard


# def get_input():
#     """
#     Retrieves and validates this program's argument.
#     Returns:
#         n: (int) the size of the chessboard.
#     """
#     global n
#     n = 0
#     if len(sys.argv) != 2:
#         print("Usage: nqueens N")
#         sys.exit(1)
#     try:
#         n = int(sys.argv[1])
#     except Exception:
#         print("N must be a number")
#         sys.exit(1)
#     if n < 4:
#         print("N must be at least 4")
#         sys.exit(1)
#     return n


# def is_attacking(pos0, pos1):
#     """
#     The positions of two queens are in an attacking mode.
#     Args:
#         pos0 (list or tuple): 1st queen's position.
#         pos1 (list or tuple): 2ndqueen's position.
#     Returns:
#         bool: True if the queens are in an attacking position else False.
#     """
#     if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
#         return True
#     return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


# def group_exists(group):
#     """
#     Checks if a group exists in the list of solutions.
#     Args:
#         group (list of integers): A group of possible positions.
#     Returns:
#         bool: True if it exists, otherwise False.
#     """
#     global solutions
#     for stn in solutions:
#         i = 0
#         for stn_pos in stn:
#             for grp_pos in group:
#                 if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
#                     i += 1
#         if i == n:
#             return True
#     return False


# def build_solution(row, group):
#     """
#     Builds a solution for the n queens problem.
#     Args:
#         row (int): The current row in the chessboard.
#         group (list of lists of integers): The group of valid positions.
#     """
#     global solutions
#     global n
#     if row == n:
#         temp_0 = group.copy()
#         if not group_exists(temp_0):
#             solutions.append(temp_0)
#     else:
#         for col in range(n):
#             a = (row * n) + col
#             matches = zip(list([pos[a]]) * len(group), group)
#             used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
#             group.append(pos[a].copy())
#             if not any(used_positions):
#                 build_solution(row + 1, group)
#             group.pop(len(group) - 1)


# def get_solutions():
#     """
#     Gets the solutions for the given chessboard size.
#     """
#     global pos, n
#     pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
#     a = 0
#     group = []
#     build_solution(a, group)


# n = get_input()
# get_solutions()
# for solution in solutions:
#     print(solution)


def get_input():
    """
    Retrieves and validates user's argument.
    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    """
    Recursively solve N-Queens problem
    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n)
            board[i][col] = 0


def main():
    n = get_input()
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()