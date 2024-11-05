import math
import os
import random
import time

GRID_SIZE = 20
GRID_CENTER = GRID_SIZE // 2
MOVE_SPEED = 1
TURN_SPEED = 45  # Increased for better control
GOAL_REWARD = 10
COLLISION_PENALTY = 5


class RoverGame:
    def __init__(self):
        self.east = 0
        self.north = 0
        self.orientation = 0
        self.score = 0
        self.goal = self.generate_goal()
        self.obstacles = self.generate_obstacles(5)
        self.running = True

    def generate_goal(self):
        return (
            random.randint(-GRID_CENTER + 2, GRID_CENTER - 2),
            random.randint(-GRID_CENTER + 2, GRID_CENTER - 2),
        )

    def generate_obstacles(self, num):
        obstacles = set()
        for _ in range(num):
            obs = (
                random.randint(-GRID_CENTER + 2, GRID_CENTER - 2),
                random.randint(-GRID_CENTER + 2, GRID_CENTER - 2),
            )
            if obs != (0, 0) and obs != self.goal:
                obstacles.add(obs)
        return obstacles

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def draw_grid(self):
        grid_x = int(GRID_CENTER + self.east)
        grid_y = int(GRID_CENTER - self.north)

        direction_chars = {
            0: "↑",
            45: "↗",
            90: "→",
            135: "↘",
            180: "↓",
            225: "↙",
            270: "←",
            315: "↖",
        }
        closest_direction = min(
            direction_chars.keys(),
            key=lambda x: abs((self.orientation - x + 180) % 360 - 180),
        )
        rover_char = direction_chars[closest_direction]

        self.clear_screen()
        print("+" + "-" * (GRID_SIZE + 1) + "+")
        for y in range(GRID_SIZE):
            print("|", end="")
            for x in range(GRID_SIZE):
                game_x = x - GRID_CENTER
                game_y = GRID_CENTER - y

                if x == grid_x and y == grid_y:
                    print(rover_char, end="")
                elif (game_x, game_y) == self.goal:
                    print("G", end="")
                elif (game_x, game_y) in self.obstacles:
                    print("X", end="")
                elif x == GRID_CENTER and y == GRID_CENTER:
                    print("+", end="")
                elif x == GRID_CENTER:
                    print("|", end="")
                elif y == GRID_CENTER:
                    print("-", end="")
                else:
                    print(" ", end="")
            print("|")
        print("+" + "-" * (GRID_SIZE + 1) + "+")

        print(f"Position: ({round(self.east, 1)}, {round(self.north, 1)})")
        print(f"Orientation: {round(self.orientation)}°")
        print(f"Score: {self.score}")
        print("\nControls:")
        print("W: Move Forward")
        print("S: Move Backward")
        print("A: Turn Left")
        print("D: Turn Right")
        print("Q: Quit")

    def move(self, meters, is_reverse=False):
        angle_rad = math.radians(self.orientation + (180 if is_reverse else 0))

        new_east = self.east + meters * math.sin(angle_rad)
        new_north = self.north + meters * math.cos(angle_rad)

        if abs(new_east) < GRID_CENTER - 1 and abs(new_north) < GRID_CENTER - 1:
            grid_x = int(new_east)
            grid_y = int(new_north)
            if (grid_x, grid_y) not in self.obstacles:
                self.east = new_east
                self.north = new_north
            else:
                self.score -= COLLISION_PENALTY
                print(f"\nHit obstacle! -{COLLISION_PENALTY} points")
                time.sleep(0.5)

    def turn(self, degrees):
        self.orientation = (self.orientation + degrees) % 360

    def check_goal(self):
        if abs(self.east - self.goal[0]) < 1 and abs(self.north - self.goal[1]) < 1:
            self.score += GOAL_REWARD
            print(f"\nGoal reached! +{GOAL_REWARD} points")
            time.sleep(1)
            self.goal = self.generate_goal()

    def run(self):
        while self.running:
            self.draw_grid()

            command = input("\nEnter command (WASD/Q): ").lower()

            if command == "q":
                self.running = False
            elif command == "w":
                self.move(MOVE_SPEED)
            elif command == "s":
                self.move(MOVE_SPEED, True)
            elif command == "a":
                self.turn(-TURN_SPEED)
            elif command == "d":
                self.turn(TURN_SPEED)

            self.check_goal()

        print("\nGame Over!")
        print(f"Final Score: {self.score}")


if __name__ == "__main__":
    game = RoverGame()
    game.run()
