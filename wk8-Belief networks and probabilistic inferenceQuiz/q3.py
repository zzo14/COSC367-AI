from itertools import *

def joint_prob(network, assignment):
    result = 1
    for name, boolean in assignment.items():
        if len(network[name]['Parents']) == 0:
            if boolean:
                result *= network[name]['CPT'][()]
            else:
                result *= 1 - network[name]['CPT'][()]
        else:
            tName, tBool = network[name]['Parents'], []
            for i in range(len(tName)):
                tBool.append(assignment[tName[i]])
            if boolean:
                result *= network[name]['CPT'][tuple(tBool)]
            else:
                result *= 1 - network[name]['CPT'][tuple(tBool)]
    return result


def query(network, query_var, evidence):
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    result = {}
    for boolean in [True, False]:
        temp = 0
        for values in product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}   
            hidden_assignments.update({query_var: boolean})
            hidden_assignments.update(evidence)
            temp += joint_prob(network, hidden_assignments)
        result[boolean] = temp
    total = sum(i for i in result.values())
    for a, b in result.items():
        result[a] = b/total
    return result


#q3
network = {
    'Disease': {
        'Parents': [],
        'CPT': {
            (): 0.00001
            }},

    'Test': {
        'Parents': ['Disease'],
        'CPT': {
            (True,): 0.99,
            (False,): 0.01,
            }},
    }


answer = query(network, 'Disease', {'Test': False})
print("The probability of having the disease\n"
      "if the test comes back positive: {:.8f}"
      .format(answer[True]))

#q4
network = {
    'Virus': {
        'Parents': [],
        'CPT': {
            (): 0.01
            }},

    'A': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.95,
            (False,): 0.1,
            }},
    
    'B': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.90,
            (False,): 0.05,
            }},    
    }


answer = query(network, 'Virus', {'A': True})
print("The probability of carrying the virus\n"
      "if test A is positive: {:.5f}"
      .format(answer[True]))