def get_shape():
    valid_shapes = [
        "square",
        "triangle",
        "triangle reversed",
        "triangle multiplication",
        "pyramid",
        "triangle prime",
    ]
    while True:
        shape = input("Enter shape: ").strip().lower()
        if shape in valid_shapes:
            return shape
        print("Invalid shape. Please enter a valid shape.")


def get_height():
    while True:
        try:
            height = int(input("Enter height: "))
            if 1 <= height <= 80:
                return height
            else:
                print("Height must be between 1 and 80.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def draw_square(height):
    for i in range(1, height + 1):
        print(" ".join([str(i)] * height))


def draw_triangle_reversed(height):
    for i in range(height):
        start = height - i
        numbers = [str(j) for j in range(start, 0, -1)]
        print(" ".join(numbers))


def draw_triangle(height):
    for i in range(1, height + 1):
        # numbers = [str(j) for j in range(1, i + 1)]
        for j in range(1, i + 1):
            print(j, end="")
        print()


def draw_triangle_multiplication(height):
    for i in range(1, height + 1):
        row = " ".join(str(i * (j + 1)) for j in range(i))
        print(row)


def draw_pyramid(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        numbers = " ".join([str(i)] * (2 * i - 1))
        print(spaces + numbers)


def draw_triangle_prime(height):
    primes = []
    candidate = 2
    total_needed = height * (height + 1) // 2
    while len(primes) < total_needed:
        is_prime = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    index = 0
    for i in range(1, height + 1):
        row_primes = primes[index : index + i]
        print(" ".join(map(str, row_primes)))
        index += i


def draw(shape, height):
    if shape == "square":
        draw_square(height)
    elif shape == "triangle":
        draw_triangle(height)
    elif shape == "triangle reversed":
        draw_triangle_reversed(height)
    elif shape == "triangle multiplication":
        draw_triangle_multiplication(height)
    elif shape == "pyramid":
        draw_pyramid(height)
    elif shape == "triangle prime":
        draw_triangle_prime(height)


def tower_of_hanoi(n, source, auxiliary, target):
    moves = []
    if n == 1:
        moves.append((source, target))
    else:
        moves += tower_of_hanoi(n - 1, source, target, auxiliary)
        moves.append((source, target))
        moves += tower_of_hanoi(n - 1, auxiliary, source, target)
    return moves


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)
