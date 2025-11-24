
def get_book_text(filePath):
    with open(filePath) as file:
        file_contents = file.read()
        words = file_contents.split()
        return len(words)


def main():
    # path = input("Enter the full path to the book text file:")
    path = "./books/frankenstein.txt"
    print("Found", get_book_text(path), "total words")

if __name__ == "__main__":
    main()