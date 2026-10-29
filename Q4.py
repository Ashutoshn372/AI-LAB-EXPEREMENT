#4.Write a program to implement A* Algorithm.

import ast
from heapq import heappush, heappop


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    came_from = {}

    heappush(open_set, (f_score[start], start))

    while open_set:
        _, current = heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)

            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            if grid[nx][ny] == 1:
                continue

            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heappush(open_set, (f_score[neighbor], neighbor))

    return None


if __name__ == "__main__":
    grid_str = input("Enter grid as a list of lists (0 = free, 1 = wall):\n")
    grid = ast.literal_eval(grid_str)
    start = ast.literal_eval(input("Enter start position as a tuple (row, col): "))
    goal = ast.literal_eval(input("Enter goal position as a tuple (row, col): "))

    path = a_star(grid, start, goal)
    if path is None:
        print("No path found.")
    else:
        print("Shortest path:", path)
