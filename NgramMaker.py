import random


class Ngram:
    def __init__(self, n, text):
        self.map = dict()
        self.n = n
        self.text = text
        self.generateMap()

    def generateMap(self):
        for depth in range(2, self.n+1):
            print(f"Generating {depth}-gram")
            for idx in range(0, len(self.text) - depth - 2):
                subarray = tuple(self.text[idx:(idx + depth - 1)])
                if self.map.get(subarray) != None:
                    self.map[subarray].insert(len(self.map[subarray]), self.text[idx + depth - 1])
                else:
                    self.map[subarray] = [self.text[idx + depth - 1]]



    def getPossibility(self, past):
        temp = len(past)
        while temp:
            possibilities = self.map.get(tuple(past[-temp:]))
            if possibilities == None:
                temp -= 1
                continue
            if len(possibilities) != 0:
                next = possibilities[random.randint(0, len(possibilities)-1)]
                return next