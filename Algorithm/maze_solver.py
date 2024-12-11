class MazeSolver:
    def __init__(self, maze):
        """
        Initialize the maze solver

        Args:
            maze (list of lists): 2D representation of the maze
                - 0 represents open path
                - 1 represents wall
                - 'S' represents start point
                - 'E' represents end point
        """
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.path = []

    def is_valid_move(self, x, y):
        """
        Check if the move is valid

        Args:
            x (int): Row coordinate
            y (int): Column coordinate

        Returns:
            bool: Whether the move is valid
        """
        # TODO: Implement move validation logic
        # Consider:
        # - Within maze boundaries
        # - Not a wall
        # - Not previously visited
        pass

    def find_start_position(self):
        """
        Find the starting position in the maze

        Returns:
            tuple: Coordinates of start position
        """
        # TODO: Locate 'S' in the maze grid
        pass

    def dfs(self, x, y):
        """
        Depth-First Search to solve the maze

        Args:
            x (int): Current row
            y (int): Current column

        Returns:
            bool: Whether a path to the end is found
        """
        # TODO: Implement DFS algorithm
        # Key considerations:
        # - Mark current position as visited
        # - Check if reached end point
        # - Explore possible moves (up, down, left, right)
        # - Backtrack if no valid moves
        pass

    def solve(self):
        """
        Main method to solve the maze

        Returns:
            list: Path from start to end, or None if no path exists
        """
        # TODO: Initialize starting point
        # TODO: Run DFS from start position
        # TODO: Return path if found
        pass


# Example maze usage
def main():
    # Example maze layout
    maze = [
        ["S", 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, "E"],
    ]

    solver = MazeSolver(maze)
    solution = solver.solve()

    if solution:
        print("Path found:", solution)
    else:
        print("No path exists")


if __name__ == "__main__":
    main()
