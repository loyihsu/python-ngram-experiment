import re


def read_file(filepath):
    file = open(filepath)
    return text_processor(file.readlines())


def text_processor(strings):
    output = []
    for string in strings:
        string = re.sub('[^A-Za-z ,.!?]', '', string)
        sentence = string.split()
        if len(sentence) != 0:
            for text in sentence:
                output.insert(len(output), text.lower())
    return output
