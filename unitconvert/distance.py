"""
A python module containing 2 functions for converting miles to kilometers and kilometers to miles.
"""


def miles_to_kilometers(L_miles):
    """
    Convert length in miles to length in kilometers.
    
    PARAMETERS
    ----------
    L_miles: tuple
        A miles expression of length
    
    RETURNS
    ----------
    L_kilometers: float
        The kilometers expression of length L_miles
    """
    
    return  1.609344*L_miles

def kilometers_to_miles(L_kilometers):
    """
    Convert length in kilometers to length in miles.
    
    PARAMETERS
    ----------
    L_kilometers: tuple
        A kilometers expression of length
    
    RETURNS
    ----------
    L_miles: float
        The miles expression of length L_kilometers
    """
    
    return  0.621371192*L_kilometers