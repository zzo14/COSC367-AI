def depth(expression,x=0):
    if not expression or not isinstance(expression,list):
        return x
    l = depth(expression[0],x + 1)
    r = depth(expression[1:],x)

    return max(l,r)