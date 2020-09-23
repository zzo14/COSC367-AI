network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    
# add more variables
    'B': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    
    'C': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    
    'D': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.4,
            (False,): 0.1,
            }
        
    },
    
    'E': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.6,
            }
        
    },    

}


print(sorted(network.keys()))
