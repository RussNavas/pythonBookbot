def word_count(txt):
    """
        a function that takes in the text of a book as a string
        and returns the number of words with a message.
        :params: a string that is the text of a book
        :returns: a string with the word count
    """
    arr = txt.split()
    return "Found " + str(len(arr)) + " total words"


def count_char(txt):
    """
    creates a frequency map of characters and symbols
    :params: text from a book
    :returns; a dict of char/symbols and their counts.
    """
    char_count = {}  # str: char: int: count
    txt = txt.lower()

    for c in txt:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    return char_count


def dict_sort(char_count):
    arr = []
    for k, v in char_count.items():
        if (k.isalpha()):
            arr.append({"char": k, "num": v})

    def sort_on(dict):
        return dict["num"]

    arr.sort(reverse=True, key=sort_on)

    for dict in arr:
        char = dict["char"]
        val = dict["num"]
        print(f"{char}: {val}")

