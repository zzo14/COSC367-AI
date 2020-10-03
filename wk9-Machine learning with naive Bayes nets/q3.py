import csv

def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]    
        spam, not_spam = 0, 0
        for i in training_examples:
            if i[-1] == '1':
                spam += 1
            elif i[-1] == '0':
                not_spam += 1
        return (spam + pseudo_count)/(spam + pseudo_count + not_spam + pseudo_count)
    

prior = learn_prior("spam-labelled.csv")
print("Prior probability of spam is {:.5f}.".format(prior))