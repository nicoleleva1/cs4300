import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from task6 import count_words

# check the word counter works on our text file
def test_word_count():
    file_path = os.path.join(os.path.dirname(__file__), "..", "task6_read_me.txt")
    count = count_words(file_path)
    assert count > 0