import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from task3 import check_sign, first_n_primes, sum_1_to_100

# test the if/elif/else function
def test_positive_number():
    assert check_sign(5) == "positive"

def test_negative_number():
    assert check_sign(-5) == "negative"

def test_zero():
    assert check_sign(0) == "zero"

# test the for loop that finds primes
def test_primes():
    primes = first_n_primes(10)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# test the while loop that adds 1 to 100
def test_sum():
    assert sum_1_to_100() == 5050