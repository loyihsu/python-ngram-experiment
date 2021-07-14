import random

import NgramMaker
import TextReader

n = 4  # N of the N-gram

file = TextReader.read_file("txt/shakespeare.txt")  # Input text file.
gram = NgramMaker.Ngram(n, file)  # Generate the N-gram

output = []

while len(output) < 400:  # Generate the first 400 words from the N-gram
    if len(output) == 0:
        output.insert(0, file[random.randint(0, len(file) - 1)])  # Start from a random word if no starting words

    if len(output) < n - 1:  # First n-1 words
        output.insert(len(output), gram.get_possibility(output))
    else:  # The rest of the thing.
        output.insert(len(output), gram.get_possibility(output[-n + 1:]))


# Generate the strings to print
def generate_printing_texts(array):
    temp = ""
    for string in array:
        temp += f"{string} "
    return temp


print(generate_printing_texts(output))
