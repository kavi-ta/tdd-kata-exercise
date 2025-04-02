import pytest
from string_calculator import string_calculator

def test_add():
    assert string_calculator("") == 0
    assert string_calculator("  ")==0
    assert string_calculator("1")==1
    assert string_calculator("1,2")==3
    assert string_calculator("10")==10
    assert string_calculator("200")==200
    with pytest.raises(ValueError) as excinfo:
        string_calculator(",")
    assert str(excinfo.value)== "Invalid Input"