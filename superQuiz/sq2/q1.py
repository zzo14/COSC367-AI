def is_valid_expression(object, function_symbols, leaf_symbols):
    if type(object) == int or type(object) == str:
        if str(object).isdigit() or object in leaf_symbols:
            return True
        else:
            return False
    elif type(object) == list:
        if len(object) != 3 or object[0] not in function_symbols:
            return False  
        elif object[0] in function_symbols:
            return True
        else:
            for elements in object:
                a = is_valid_expression(elements, function_symbols, leaf_symbols)
            return a
    else:
        return False