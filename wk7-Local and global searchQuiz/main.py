from q4 import n_queens_neighbours as neighbours, n_queens_cost as cost
from q4 import greedy_descent, greedy_descent_with_random_restart
import random

N = 6
random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))   

greedy_descent_with_random_restart(random_state, neighbours, cost)