def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
   
    diction = dict(zip(key,value))
    
    return diction

key = [1, 2, 3] 
value = ["one", "two", "three"]
print(create_dictionary(key, value))