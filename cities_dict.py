def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    cities_dict = {}
    for kalit, qiymat in enumerate(cities):
        cities_dict[kalit] = qiymat
    return cities_dict