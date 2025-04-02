import pytest
from string_calculator import string_calculator

def test_add():
    assert string_calculator("") == 0
    assert string_calculator("  ")==0