import string

def clean_string(s: str):
    """
    Removes punctuation and whitespaces
    """
    to_remove = string.punctuation + string.whitespace
    mapping = {ord(c): None for c in to_remove}
    return s.translate(mapping)

def strings_almost_equal(s1: str, s2: str):
    """ 
    Compares strings up to punctuation and whitespaces.
    """
    return clean_string(s1) == clean_string(s2)