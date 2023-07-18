def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    mirka= ''
    age=0
    for i in data:
        if i['age']>age:
            age=i['age']
            mirka=i['name']
    return mirka
print(get_max_age_user_name(data))
    