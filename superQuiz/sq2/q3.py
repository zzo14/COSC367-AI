def evaluate(expression, bindings):
    if type(expression) != list:
        if type(expression) == int:
            return expression
        else:
            return bindings[expression]
    else:          
        return bindings[expression[0]](evaluate(expression[1], bindings), evaluate(expression[2], bindings))

import operator

bindings = {'x': 5, 'y': 10, 'blah': 15, '+': lambda x, y: x + y}
expression = ['+', ['+', 22, 'y'], 'x']
print(evaluate(expression, bindings))

for i in range(4):
    bindings['y'] += 1
    print(bindings)
    