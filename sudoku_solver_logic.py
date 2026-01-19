def is_valid(board, row, col, num):
    """
    Check if it's valid to place the number in the given row and column.

    :param board: 2D list representing the Sudoku board
    :param row: Row index
    :param col: Column index
    :param num: Number to be placed
    :return: True if valid, False otherwise
    """
    # Check if the number is not repeated in the current row
    if num in board[row]:
        return False

    # Check if the number is not repeated in the current column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is not repeated in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking.

    :param board: 2D list representing the Sudoku board
    :return: True if the board is solved, False otherwise
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0  # Reset and backtrack

                return False  # Trigger backtracking

    return True  # Puzzle solved

def print_board(board):
    """
    Print the Sudoku board in a readable format.

    :param board: 2D list representing the Sudoku board
    """
    for row in range(9):
        for col in range(9):
            if col == 8:
                print(board[row][col])
            else:
                print(board[row][col], end=" ")
        if row % 3 == 2 and row != 8:
            print("-" * 21)

def main():
    # Example Sudoku puzzle (0 represents empty cells)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    # Try to solve the Sudoku puzzle
    if solve_sudoku(sudoku_board):
        print("Sudoku solved successfully:")
        print_board(sudoku_board)
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()