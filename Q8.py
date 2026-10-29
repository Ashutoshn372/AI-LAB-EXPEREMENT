#8. Write a program to solve the Water Jug Problem.

from collections import deque


def water_jug_problem(cap_a, cap_b, target):
    start = (0, 0)
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    action = {start: None}

    while queue:
        state = queue.popleft()
        x, y = state

        if x == target or y == target:
            path = []
            while state is not None:
                path.append((state, action[state]))
                state = parent[state]
            path.reverse()
            return path

        moves = [
            ((cap_a, y), 'Fill jug A'),
            ((x, cap_b), 'Fill jug B'),
            ((0, y), 'Empty jug A'),
            ((x, 0), 'Empty jug B'),
            ((max(0, x - (cap_b - y)), min(cap_b, y + x)), 'Pour A into B'),
            ((min(cap_a, x + y), max(0, y - (cap_a - x))), 'Pour B into A')
        ]

        for next_state, description in moves:
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = state
                action[next_state] = description
                queue.append(next_state)

    return None


if __name__ == "__main__":
    cap_a = int(input("Enter capacity of jug A: "))
    cap_b = int(input("Enter capacity of jug B: "))
    target = int(input("Enter target amount: "))

    path = water_jug_problem(cap_a, cap_b, target)
    if path is None:
        print("No solution found.")
    else:
        print("Solution steps:")
        for state, step in path:
            print(state, '->', step)
