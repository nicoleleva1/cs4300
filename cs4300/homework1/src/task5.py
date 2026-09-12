# a list of tuples, each holding a book title and its author
books = [
    ("Dune", "Frank Herbert"),
    ("1984", "George Orwell"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Foundation", "Isaac Asimov"),
    ("Brave New World", "Aldous Huxley"),
]

# uses list slicing to return just the first three books
def first_three_books():
    return books[:3]

# a dictionary mapping student names to their student ID numbers
students = {
    "Alice": 1001,
    "Bob": 1002,
    "Carla": 1003,
}