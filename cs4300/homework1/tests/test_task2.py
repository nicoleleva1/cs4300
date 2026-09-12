import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from task2 import get_integer, get_float, get_string, get_boolean

# Making sure each function returns the correct type

def test_integer():
    num = get_integer()
    assert type(num) == int

def test_float():
    num = get_float()
    assert type(num) == float

def test_string():
    text = get_string()
    assert type(text) == str

def test_boolean():
    val = get_boolean()
    assert type(val) == bool