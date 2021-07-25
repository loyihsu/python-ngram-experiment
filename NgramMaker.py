import random


class Ngram:
    def __init__(self, n, text):
        self.map = dict()
        self.n = n
        self.text = text
        self.generate_map()

    # Create an N-gram dictionary for the input text.
    def generate_map(self):
        for depth in range(2, self.n + 1):
            print(f"Generating {depth}-gram")
            for idx in range(0, len(self.text) - depth - 2):
                subarray = tuple(self.text[idx:(idx + depth - 1)])
                if self.map.get(subarray) is not None:
                    self.map[subarray].append(self.text[idx + depth - 1])
                else:
                    self.map[subarray] = [self.text[idx + depth - 1]]

    # Quick getter of the next random word.
    def get_possibility(self, past):
        temp = len(past)
        while temp:
            possibilities = self.map.get(tuple(past[-temp:]))
            if possibilities is None:
                temp -= 1
                continue
            if len(possibilities) != 0:
                return possibilities[random.randint(0, len(possibilities) - 1)]
