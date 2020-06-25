""" Tools and utilities used specifically for forms. """

def pick_from_dict(input_dict, *args):
    """ Take items from a dict to build a new dict. Delete the items
    in the original.
    
    :param input_dict: the dict to operate on.
    :param *args: the keys to pick.
    :return: The new dict and the old dict as a tuple.
    """
    filtered_dict = {}
    for key in args:
        try:
            filtered_dict[key] = input_dict[key]
            del input_dict[key]
        except KeyError:
            pass
    return filtered_dict, input_dict

def popget(input_dict, key, default):
    """ Pop and get combined. """

    try:
        value = input_dict.pop(key)
    except KeyError:
        value = default
    return value
