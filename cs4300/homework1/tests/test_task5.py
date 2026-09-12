import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from task5 import first_three_books, students

# check that slicing gives us exactly 3 books
def test_first_three_books():
    result = first_three_books()
    assert len(result) == 3

# check the dictionary has the right info
def test_students_dict():
    assert students["Alice"] == 1001