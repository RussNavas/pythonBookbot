import sys
from stats import word_count, count_char, dict_sort


def get_book_text(path):
    """
        a funciton to read in the text of a book as a string
        :params: a relative path
        :returns: a string
    """
    with open(path) as f:
        txt = f.read()
        return txt


def main():
    """
        The entry point into the program
    """

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    txt = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(word_count(txt))
    print("--------- Character Count -------")
    dict_sort(count_char(txt))
    print("============= END ===============")


main()
