def roulette_wheel_select(population, fitness, r):
    total = sum(fitness(x) for x in population)
    c = 0
    
    for p in population:
        c += fitness(p)
        if total * r < c:
            return p




population = ['a', 'b']

def fitness(x):
    return 1 # everyone has the same fitness

for r in [0, 0.33, 0.49999, 0.5, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))