"""
A python module containing 2 functions for converting fahrenheit to celsius and celsius to fahrenheit.
"""


def fahrenheit_to_celsius(T_fahrenheit):
    """
    Convert fahrenheit temperature to celsius temperature.
    
    PARAMETERS
    ----------
    T_fahrenheit: tuple
        A fahrenheit expression of temperature
    
    RETURNS
    ----------
    T_celsius: float
        The celsius expression of temperature T_fahrenheit
    """
    
    return  (T_fahrenheit-32)*5/9

def celsius_to_fahrenheit(T_celsius):
    """
    Convert celsius temperature to fahrenheit temperature.
    
    PARAMETERS
    ----------
    T_celsiu: tuple
        A celsius expression of temperature
    
    RETURNS
    ----------
    T_fahrenheit: float
        The fahrenheit expression of temperature T_celsius
    """
    
    return  T_celsius*9/5+32