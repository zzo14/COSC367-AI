import operator

def generate_rest(initial, expression, length):
    if length <= 0:
        return []
    elif type(expression) == int:
        result = []
        while length != 0:
            result.append(expression)
            length -= 1
        return result  
    elif expression == 'i':
        i = len(initial)
        result = []
        while length != 0:
            result.append(i)
            length -= 1
            i += 1
        return result
    elif expression == 'x':
        result = initial
        while len(result) < length:
            result += initial
        return result[:length]
    elif expression == 'y':
        result = []
        while length != 0:
            result.append(initial[-1])
            length -= 1
        return result 
    else:
        result = []
        bindings = {"x":initial[-2], "y":initial[-1], "i":len(initial), "+":lambda x, y: x + y, "-":lambda x, y: x - y, "*":lambda x, y: x * y, "/":lambda x, y: x / y}
        while length != 0:
            result.append(evaluate(expression, bindings))
            bindings["x"] = bindings["y"]
            bindings["y"] = result[len(result)-1]
            bindings["i"] += 1
            length -= 1
        return result
    
   
def evaluate(expression, bindings):
    if type(expression) != list:
        if type(expression) == int:
            return expression
        else:
            return bindings[expression]
    else:          
        return bindings[expression[0]](evaluate(expression[1], bindings), evaluate(expression[2], bindings))
   
   
    
initial_sequence = [4, 6, 8, 10]
expression = ['*', ['+', 'i', 2], 2]
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))