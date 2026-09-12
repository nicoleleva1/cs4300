import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from task1 import hello_world

# Check that the function prints the right thing
def test_hello_world(capsys):
    hello_world()
    output = capsys.readouterr()
    assert output.out == "Hello, World!\n"