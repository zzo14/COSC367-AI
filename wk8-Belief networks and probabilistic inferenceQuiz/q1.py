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
    



network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': True})
print("{:.5f}".format(p))


network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': False})
print("{:.5f}".format(p))


network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
p = joint_prob(network, {'A': False, 'B':True})
print("{:.5f}".format(p)) 