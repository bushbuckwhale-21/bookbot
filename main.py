from stats import get_num_words
from stats import get_char_frequencies

def main():
    # path = input("Enter the full path to the book text file:")
    path = "./books/frankenstein.txt"
    print(get_char_frequencies(path))

if __name__ == "__main__":
    main()