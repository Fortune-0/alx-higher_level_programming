#!/usr/bin/python3

def add_integer(a, b=98):
    '''
        Add two integers. If no second argument is provided, use 98 as the default value for b.
        
        args
        a = first argument a
        b = second argument b
    '''
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    ''' the above line of checks if the supplied arguments is either an
        integer or a float. if not raise an error message that a or b must be an integer
        or a float.
    '''
    
    #a = int(a) #if a float is passed convert a to an integer
    #b = int(b) #if a float is passed convert b to an integer
    
    #sums a and b together
    return int(a) + int(b)

