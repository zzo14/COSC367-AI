import csv

def learn_likelihood(file_name, pseudo_count=0):
    result = []
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]  
    for i in range(12):
        tt, tf, ft, ff = 0, 0, 0, 0
        for j in training_examples:
            if (j[i], j[-1]) == ("1", "1"):
                tt += 1
            elif (j[i], j[-1]) == ("1", "0"):
                tf += 1
            elif (j[i], j[-1]) == ("0", "1"):
                ft += 1
            elif (j[i], j[-1]) == ("0", "0"):
                ff += 1
        f = (tf + pseudo_count)/(tf + ff + pseudo_count*2)
        t = (tt + pseudo_count)/(ft + tt + pseudo_count*2)
        result.append([f, t])
    return result

likelihood = learn_likelihood("spam-labelled.csv")

print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))