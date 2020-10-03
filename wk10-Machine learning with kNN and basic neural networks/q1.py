import math
#q1
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

print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))
print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
print(majority_element("ababc") in "ab")