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






def cost(x):
    return -x**2

def neighbours(x):
    return [x - 1, x + 1] if abs(x) < 5 else []

for state in greedy_descent(0, neighbours, cost):
    print(state)