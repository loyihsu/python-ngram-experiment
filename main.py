import NgramMaker
import TextReader

n = 10

file = TextReader.readTexts("txt/shakespeare.txt")
gram = NgramMaker.Ngram(n, file)

output = ["In", "the"]

while len(output) < 400:
    if len(output) < n-1:
        output.insert(len(output), gram.getPossibility(output))
    else:
        output.insert(len(output), gram.getPossibility(output[-n+1:]))

printed = ""

for string in output:
    printed += f"{string} "

print(printed)