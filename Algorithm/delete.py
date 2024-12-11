import sys


def is_valid(grid, row, col, num):
    size = 9

    if num in grid[row]:
        return False

    if num in (grid[i][col] for i in range(size)):
        return False

    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == num:
                return False
    return True


def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


# Backtracking solver
def solve_sudoku(grid):

    empty = find_empty_cell(grid)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Undo the placement (backtrack)

    return False  # Trigger backtracking


# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))


# Example Sudoku puzzle
grid = []


if len(sys.argv) < 2:
    print("Please provide the file name containing the Sudoku puzzle.")
    sys.exit(1)
filename = sys.argv[1]
with open(filename, "r") as f:
    for line in f:
        rows = []
        for r in line.strip().split():
            rows.append(int(r))
        grid.append(rows)
print("Original Sudoku Puzzle:")
print_grid(grid)
if solve_sudoku(grid):
    print("\nSolved Sudoku Puzzle:")
    print_grid(grid)
else:
    print("\nNo solution exists for the given Sudoku puzzle.")
