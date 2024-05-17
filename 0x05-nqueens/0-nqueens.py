#!/usr/bin/python3
"""
N queens
"""


from sys import argv


def print_error_message(message):
    print(message)
    exit(1)


# Validate input
if len(argv) != 2:
    print_error_message("Usage: nqueens N")
    exit(1)
try:
    n = int(argv[1])
except ValueError:
    print_error_message('N must be a number')
    exit(1)
if n < 4:
    print_error_message('N must be at least 4')
    exit(1)

board = [[0 for _ in range(n)] for _ in range(n)]
answer = []


def isSafe(board, n, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQutil(board, n, col, solutions):
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[j][i] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if isSafe(board, n, i, col):
            board[i][col] = 1

            if solveNQutil(board, n, col+1, solutions):
                return True
            board[i][col] = 0
    return False


def solveNqueen():
    solutions = []
    solveNQutil(board, n, 0, solutions)
    # if not solutions:
    #     print('Not found')
    # else:
    for solution in solutions:
        print(solution)


solveNqueen()
