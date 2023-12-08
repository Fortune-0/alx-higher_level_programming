#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    '''this function prints out the first 
    last name of the user
    '''
    if not isinstance(first_name, str) or not isinstance (last_name, str):
        #checks if first_name and last_name is a string
        raise TypeError ("first_name must be a string")
    TypeError ("last_name must be a string")
    # raise a TypeError is first_name or last_name is not a string
    
    print("My name is {} {}".format(first_name, last_name))
    #return (first_name, last_name)
