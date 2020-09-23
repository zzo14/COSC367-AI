from itertools import combinations

def n_queens_neighbours(state):
    neighbours = []
    for i , j in combinations(range(len(state)), 2):
        neighbour = list(state)
        neighbour[i], neighbour[j] =  state[j], state[i]
        neighbours.append(tuple(neighbour))
    return sorted(neighbours)
        


print(n_queens_neighbours((1, 3, 2)))