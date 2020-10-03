import math
#q2
def euclidean_distance(v1, v2):
    return math.sqrt(sum((i - j)**2 for i, j in zip(v1, v2)))

def majority_element(labels):
    freq_max = {}
    for i in labels:
        try:
            freq_max[i] += 1
        except KeyError:
            freq_max[i] = 1
    for key,value in freq_max.items():
        if value == max(freq_max.values()):
            return key

def knn_predict(input, examples, distance, combine, k):
    eg_list, result, mark = [], [], []
    for i, j in examples:
        eg_list.append((distance(input, i), j))
    
    for i in range(0, k):
        result.append(min(eg_list))
        eg_list.remove(min(eg_list))
    while len(eg_list)>0 and min(eg_list)[0] == max(result)[0]:
        result.append(min(eg_list))
        eg_list.remove(min(eg_list))        
        
    for i, j in result:
        mark.append(j)
    return combine(mark)
        

examples = [
    ([2], '-'),
    ([3], '-'),
    ([5], '+'),
    ([8], '+'),
    ([9], '+'),
]

distance = euclidean_distance
combine = majority_element

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print(x, knn_predict([x], examples, distance, combine, k))
    print()
    



examples = [
    ([1], 5),
    ([2], -1),
    ([5], 1),
    ([7], 4),
    ([9], 8),
]

def average(values):
    return sum(values) / len(values)

distance = euclidean_distance
combine = average

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
    print()