import pytest
from unitconvert.distance import miles_to_kilometers
from unitconvert.distance import kilometers_to_miles
from unitconvert.temperature import fahrenheit_to_celsius
from unitconvert.temperature import celsius_to_fahrenheit

def test_miles_to_kilometers():
    # some known results
    # 0 mile = 0 kilometer
    # 1 mile = 1.609344 km
    # very strict test without rtol
    assert miles_to_kilometers(0) == 0    
    assert miles_to_kilometers(1) == 1.609344

    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        miles_to_kilometers('a')
        miles_to_kilometers(1,1)
        
def test_kilometers_to_miles():
    # some known results
    # 0 km = 0 mile
    # 1 km = 0.621371192 miles
    # very strict test without rtol
    assert kilometers_to_miles(0) == 0    
    assert kilometers_to_miles(1) == 0.621371192

    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        kilometers_to_miles('a')
        kilometers_to_miles(1,2)

def test_fahrenheit_to_celsius():
    # some known results
    # 23 fahrenheit = -5 celsius
    # 14 fahrenheit = -10 celsius
    # very strict test without rtol
    assert fahrenheit_to_celsius(23) == -5
    assert fahrenheit_to_celsius(14) == -10

    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        fahrenheit_to_celsius('a')
        fahrenheit_to_celsius(1,3)
        
def test_celsius_to_fahrenheit():
    # some known results
    # 0 celsius = 32 fahrenheit
    # 25 celsius = 77 fahrenheit
    # very strict test without rtol
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(25) == 77

    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        celsius_to_fahrenheit('a')
        celsius_to_fahrenheit(1,4)