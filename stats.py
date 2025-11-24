import collections

def get_num_words(filePath):
    with open(filePath) as file:
        file_contents = file.read()
        words = file_contents.split()
        return len(words)


def get_char_frequencies(filePath):
    with open(filePath) as file:
        file_contents = file.read()
        freq = {}
        for char in file_contents:
            char = char.lower()
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
    
    return freq
        