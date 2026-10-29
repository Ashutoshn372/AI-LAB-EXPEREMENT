#Write a program to implement Depth First Search (DFS).

import ast


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start in visited:
        return []

    visited.add(start)
    traversal = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            traversal.extend(dfs(graph, neighbor, visited))

    return traversal


if __name__ == "__main__":
    graph_str = input("Enter adjacency list as a Python dictionary literal: \n")
    graph = ast.literal_eval(graph_str)
    start = input("Enter start node: ")
    print("DFS traversal from", start, ":", dfs(graph, start))
