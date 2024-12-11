def find_singles(grid):
    size = 9

    def get_possibilities(row, col):
        possible = set(range(1, 10))
        # Remove numbers from same row
        possible -= set(grid[row])
        # Remove numbers from same column
        possible -= set(grid[i][col] for i in range(size))
        # Remove numbers from same 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                possible -= {grid[i][j]}
        return possible

    # Find Naked Singles
    for row in range(size):
        for col in range(size):
            if grid[row][col] == 0:  # Empty cell
                possibilities = get_possibilities(row, col)
                if len(possibilities) == 1:  # Naked Single!
                    print(f"Naked Single found at ({row},{col}): {possibilities}")

    # Find Hidden Singles (example for rows)
    for row in range(size):
        for num in range(1, 10):
            possible_positions = []
            for col in range(size):
                if grid[row][col] == 0 and num in get_possibilities(row, col):
                    possible_positions.append(col)
            if len(possible_positions) == 1:
                print(
                    f"Hidden Single found: {num} must go in row {row}, column {possible_positions[0]}"
                )


if __name__ == "__main__":

    with open("puzzle.txt", "r") as f:
        grid = []
        for line in f:
            row = []
            for num in line.strip().split():
                row.append(int(num))
            grid.append(row)
        find_singles(grid)
