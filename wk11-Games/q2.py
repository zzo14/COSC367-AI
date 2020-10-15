def max_action_value(game_tree):
    a, v = 0, -float('inf')
    if isinstance(game_tree, list):
        for i in game_tree:
            if v < min_action_value(i)[1]:
                v = min_action_value(i)[1]
                a = game_tree.index(i)
        return a, v
    else:
        return None, game_tree
    
def min_action_value(game_tree):
    a, v = 0, float('inf')
    if isinstance(game_tree, list):
        for i in game_tree:
            if v > max_action_value(i)[1]:
                v = max_action_value(i)[1]
                a = game_tree.index(i)
        return a, v
    else:
        return None, game_tree    


game_tree = [3, [[2, 1], [4, [7, -2]]], 0]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)