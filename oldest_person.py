def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    maxi_v = 0
    maxi_k =''
    for k,v in people.items():
        if maxi_v < v:
            maxi_v = v
            maxi_k = k
    return maxi_k

people = {"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}
print(oldest(people))