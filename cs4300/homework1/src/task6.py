# opens a text file and counts how many words are in it
def count_words(filepath):
    with open(filepath, "r") as f:
        text = f.read()
    # split() breaks the text into a list of words by whitespace
    return len(text.split())