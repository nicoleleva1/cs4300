import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from task4 import calculate_discount

# test with whole numbers
def test_discount_ints():
    result = calculate_discount(100, 10)
    assert result == 90

# test with decimal numbers
def test_discount_floats():
    result = calculate_discount(50.0, 20.0)
    assert result == 40.0