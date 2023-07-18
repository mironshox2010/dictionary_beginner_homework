def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    lengh = 0
    for item  in data.values:
        lengh += len(item)
    return lengh
data = {
    1: 'a', 
    2: 'b', 
    3: 'c'
  }
print(find_max_value(data))
