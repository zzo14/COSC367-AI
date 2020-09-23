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
        



network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

answer = query(network, 'Burglary', {'John': True, 'Mary': True})
print("Probability of a burglary when both\n"
      "John and Mary have called: {:.3f}".format(answer[True])) 