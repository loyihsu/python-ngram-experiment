import re


def readTexts(filepath):
    file = open(filepath)
    return textProcessor(file.readlines())

def textProcessor(strings):
    output = []
    for string in strings:
        string = re.sub('[^A-Za-z ,.]', '', string)
        sentence = string.split()
        if len(sentence) != 0:
            for text in sentence:
                output.insert(len(output), text.lower())
    return output
