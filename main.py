
def get_book_text(filePath):
    with open(filePath) as file:
        file_contents = file.read()
        return file_contents


def main():
    # path = input("Enter the full path to the book text file:")
    path = "./books/frankenstein.txt"
    print(get_book_text(path))

if __name__ == "__main__":
    main()