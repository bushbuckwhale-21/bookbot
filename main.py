from stats import get_num_words
from stats import get_char_frequencies

def main():
    # path = input("Enter the full path to the book text file:")
    path = "./books/frankenstein.txt"
    num_words = get_num_words(path)
    frequencies = get_char_frequencies(path)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    for key, item in sorted_frequencies:
        if key.isalpha():
            print(f"{key}: {item}")

    print("============= END ===============")

if __name__ == "__main__":
    main()