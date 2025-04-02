import pytest
from string_calculator import string_calculator
from custom_exceptions import NegativeNumberException

def test_add():
    # case 1
    assert string_calculator("") == 0
    assert string_calculator("  ")==0
    assert string_calculator("1")==1
    assert string_calculator("1,2")==3
    assert string_calculator("10")==10
    assert string_calculator("200")==200
    with pytest.raises(ValueError) as excinfo:
        string_calculator(",")
    assert str(excinfo.value)== "Invalid Input"
    # case 2: handle more than 2 numbers
    assert string_calculator("1,2,3,4,5,6")==1+2+3+4+5+6
    #case 3: allow new lines between numbers
    assert string_calculator("1\n2,3")==6
    with pytest.raises(ValueError) as excinfo:
        string_calculator("1,\n")
    assert str(excinfo.value)== "Invalid Input"
    with pytest.raises(ValueError) as excinfo:
        string_calculator("1,\n2")
    assert str(excinfo.value)== "Invalid Input"
    # case 4: add a delimiter
    assert string_calculator("//;\n1;2")==3
    with pytest.raises(ValueError) as excinfo:
        string_calculator("//;\n1\n;2")
    assert str(excinfo.value)== "Invalid Input"
    assert string_calculator("//;\n3;4")==7
    with pytest.raises(ValueError) as excinfo:
        string_calculator("//!\n2!2!")
    assert str(excinfo.value)== "Invalid Input"
    # case 5 : handle negative numbers
    with pytest.raises(NegativeNumberException) as excinfo:
        string_calculator("-2")
    assert str(excinfo.value)== "negatives not allowed -2"
    with pytest.raises(NegativeNumberException) as excinfo:
        string_calculator("-2,4,-5")
    assert str(excinfo.value)== "negatives not allowed -2,-5"
    with pytest.raises(ValueError) as excinfo:
        string_calculator("//!\n-2!2!")
    assert str(excinfo.value)== "Invalid Input"
    with pytest.raises(NegativeNumberException) as excinfo:
        string_calculator("//!\n2!-2")
    assert str(excinfo.value)== "negatives not allowed -2"


