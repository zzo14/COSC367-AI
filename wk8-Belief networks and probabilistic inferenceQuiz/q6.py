network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
    'B': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.7,
            (True,): 0.3
            }},
            
    'C': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.5,
            (True,): 0.5
            }},
}