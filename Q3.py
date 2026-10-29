#Write a program to implement Hill Climbing Algorithm


def objective(x, y):
    return -(x - 3) ** 2 - (y - 4) ** 2 + 10


def hill_climbing(start=(0, 0), step_size=1):
    current = start
    current_value = objective(*current)
    path = [current]

    while True:
        best_move = current
        best_value = current_value

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue

                candidate = (current[0] + dx * step_size, current[1] + dy * step_size)
                candidate_value = objective(*candidate)

                if candidate_value > best_value:
                    best_value = candidate_value
                    best_move = candidate

        if best_move == current:
            break

        current = best_move
        current_value = best_value
        path.append(current)

    return current, current_value, path


if __name__ == "__main__":
    start_x = int(input("Enter start x: "))
    start_y = int(input("Enter start y: "))
    step = int(input("Enter step size: "))
    best_point, best_value, path = hill_climbing((start_x, start_y), step)
    print("Hill climbing path:", path)
    print("Best point:", best_point)
    print("Best value:", best_value)
