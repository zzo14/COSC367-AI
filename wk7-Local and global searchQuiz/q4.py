from itertools import combinations

def n_queens_neighbours(state):
    neighbours = []
    for i , j in combinations(range(len(state)), 2):
        neighbour = list(state)
        neighbour[i], neighbour[j] =  state[j], state[i]
        neighbours.append(tuple(neighbour))
    return sorted(neighbours)

def n_queens_cost(state):
    return len([(a, b) for (a, b) in list(combinations([(x, y) for x in state for y in [state.index(x)]], 2)) if abs(a[0] - b[0]) == abs(a[1] - b[1])])

def greedy_descent(initial_state, neighbours, cost):
    result = []
    small_cost = cost(initial_state)
    flag = True
    while flag:
        result.append(initial_state)
        neighbour = neighbours(initial_state)
        
        if len(neighbour) < 1:
            flag = False
        else:
            cost_list = [cost(i) for i in neighbour]
            smallest_cost = min(cost_list)
            if smallest_cost < small_cost:
                initial_state = neighbour[cost_list.index(smallest_cost)]
                small_cost = smallest_cost
            else:
                flag = False
    return result


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    initial_state = random_state()
    small_cost = cost(initial_state)
    while small_cost != 0:
        print(initial_state)
        neighbour = neighbours(initial_state)
        if len(neighbour) < 1:
            break
        else:
            cost_list = [cost(i) for i in neighbour]
            smallest_cost = min(cost_list)
            if smallest_cost < small_cost:
                initial_state = neighbour[cost_list.index(smallest_cost)]
                small_cost = smallest_cost
            else:
                initial_state = random_state()
                small_cost = cost(initial_state)
                print("RESTART")
    print(initial_state)
    

