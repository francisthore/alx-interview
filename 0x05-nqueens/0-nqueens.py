#!/usr/bin/python3
"""Module to implement n queens algorithm"""

import sys


def generate_solutions(board_size, board_width):
    """Generates solutions for the n-queens problem."""
    solutions = [[]]
    for row in range(board_size):
        solutions = add_queen(row, board_width, solutions)
    return solutions


def add_queen(row, board_width, previous_solutions):
    """Attempts to add a queen to each position in the current row."""
    new_solutions = []
    for solution in previous_solutions:
        for col in range(board_width):
            if is_position_safe(row, col, solution):
                new_solutions.append(solution + [col])
    return new_solutions


def is_position_safe(row, col, solution):
    """Checks if a queen can be placed safely in the current position."""
    if col in solution:
        return False
    return all(abs(solution[placed_col] - col) != row - placed_col
               for placed_col in range(row))


def initialize():
    """Initializes the board size from user input."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    board_size = int(sys.argv[1])
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def run_n_queens():
    """Main function to solve and display n-queens solutions."""
    board_size = initialize()
    solutions = generate_solutions(board_size, board_size)
    for solution in solutions:
        formatted_solution = [[row, col] for row, col in enumerate(solution)]
        print(formatted_solution)


if __name__ == "__main__":
    run_n_queens()
