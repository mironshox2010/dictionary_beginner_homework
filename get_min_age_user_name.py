def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    age=data[0]['age']
    name=''
    for i in data:
        if i['age']<=age:
            age=i['age']
            name=i['name']
    return name
print(get_min_age_user_name(data))
