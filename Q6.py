#6. Write a program to implement Alpha-Beta Pruning.

import ast


def alpha_beta(node, alpha, beta, maximizing_player):
    if isinstance(node, int):
        return node

    if maximizing_player:
        value = float('-inf')
        for child in node.values():
            value = max(value, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    value = float('inf')
    for child in node.values():
        value = min(value, alpha_beta(child, alpha, beta, True))
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value


if __name__ == "__main__":
    tree_str = input("Enter game tree as a nested dictionary (example: {'A': {'B': 5, 'C': 3}}):\n")
    game_tree = ast.literal_eval(tree_str)
    result = alpha_beta(game_tree, float('-inf'), float('inf'), True)
    print("Alpha-beta result:", result)
