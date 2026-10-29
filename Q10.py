#10. Write a program to solve the Travelling Salesman Problem.

import ast
from math import inf


def distance(city_a, city_b):
    return abs(city_a[0] - city_b[0]) + abs(city_a[1] - city_b[1])


def traveling_salesman(cities):
    city_names = list(cities.keys())
    n = len(city_names)
    if n == 1:
        return 0, [city_names[0], city_names[0]]

    dist = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = distance(cities[city_names[i]], cities[city_names[j]])

    dp = {(1 << 0, 0): 0}
    parent = {}

    for mask in range(1 << n):
        for j in range(n):
            if not (mask & (1 << j)):
                continue
            if mask == (1 << j):
                continue

            prev_mask = mask ^ (1 << j)
            if prev_mask == 0:
                continue

            for i in range(n):
                if not (prev_mask & (1 << i)):
                    continue
                new_cost = dp.get((prev_mask, i), inf) + dist[i][j]
                existing = dp.get((mask, j), inf)
                if new_cost < existing:
                    dp[(mask, j)] = new_cost
                    parent[(mask, j)] = (prev_mask, i)

    final_mask = (1 << n) - 1
    best_end = None
    best_cost = inf
    for j in range(1, n):
        cost = dp.get((final_mask, j), inf) + dist[j][0]
        if cost < best_cost:
            best_cost = cost
            best_end = j

    route = [city_names[best_end]]
    mask = final_mask
    current = best_end
    while mask != 1:
        prev_mask, prev_city = parent[(mask, current)]
        route.append(city_names[prev_city])
        mask = prev_mask
        current = prev_city

    route.reverse()

    return best_cost, route


if __name__ == "__main__":
    cities_str = input("Enter city coordinates as a dictionary like {'A': (0, 0), 'B': (1, 3)}: \n")
    cities = ast.literal_eval(cities_str)
    cost, route = traveling_salesman(cities)
    print("Minimum route cost:", cost)
    print("Route:", ' -> '.join(route))
