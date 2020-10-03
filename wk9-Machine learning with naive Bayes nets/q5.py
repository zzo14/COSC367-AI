import csv

def nb_classify(prior, likelihood, input_vector):
    certainty = posterior(prior, likelihood, input_vector)
    if certainty > 0.5:
        return ("Spam", certainty)
    else:
        return ("Not Spam", 1 - certainty)
    
    




def posterior(prior, likelihood, observation):
    t_part , f_part, normal = prior, 1-prior, 0
    for p, o in zip(likelihood, observation):
        if o:
            t, f = p[o], p[1-o]
            t_part *= t
            f_part *= f
        else:
            t, f = 1 - p[1- o], 1- p[o]
            t_part *= t
            f_part *= f            
    normal = 1/(t_part + f_part)
    return t_part*normal

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



prior = learn_prior("spam-labelled.csv")
likelihood = learn_likelihood("spam-labelled.csv")

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))