#1. Write a program to implement Breadth First Search (BFS).

import ast
from collections import deque


def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


if __name__ == "__main__":
    graph_str = input("Enter adjacency list as a Python dictionary literal (example: {'A': ['B', 'C'], 'B': ['D']}): \n")
    graph = ast.literal_eval(graph_str)
    start = input("Enter start node: ")
    print("BFS traversal from", start, ":", bfs(graph, start))
