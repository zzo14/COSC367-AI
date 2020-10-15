def max_value(tree):
    v = -float('inf')
    if isinstance(tree, list):
        for i in tree:
            v = max(v, min_value(i))
        return v
    else:
        return tree
    
def min_value(tree):
    v = float('inf')
    if isinstance(tree, list):
        for i in tree:
            v = min(v, max_value(i))
        return v
    else:
        return tree    


game_tree = [2, [-3, 1], 4, 1]

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))