#5. Write a program to implement Min-Max Algorithm.

import ast


def minimax(node, is_maximizing):
    if isinstance(node, int):
        return node

    if is_maximizing:
        return max(minimax(child, False) for child in node.values())
    return min(minimax(child, True) for child in node.values())


if __name__ == "__main__":
    tree_str = input("Enter game tree as a nested dictionary (example: {'A': {'B': 5, 'C': 3}}):\n")
    game_tree = ast.literal_eval(tree_str)
    best_value = minimax(game_tree, True)
    print("Minimax value:", best_value)
