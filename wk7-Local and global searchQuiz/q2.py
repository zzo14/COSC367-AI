from itertools import combinations

def n_queens_cost(state):
    return len([(a, b) for (a, b) in list(combinations([(x, y) for x in state for y in [state.index(x)]], 2)) if abs(a[0] - b[0]) == abs(a[1] - b[1])])



print(n_queens_cost((1, 2)))

print(n_queens_cost((1, 3, 2)))

print(n_queens_cost((1, 2, 3)))

print(n_queens_cost((1,)))

print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))

print(n_queens_cost((2, 3, 1, 4)))