class Setter:

    def __init__(self):
        self.data = [False] * 100

    def add(self, other):
        self.data[other] = True

    def remove(self, other):
        self.data[other] = False

    def contains(self, other):
        return self.data[other]


