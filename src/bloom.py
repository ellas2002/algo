
with open('../bad.txt', 'r') as file:
    BAD = [line.rstrip() for line in file]

with open('../good.txt', 'r') as file:
    GOOD = [line.rstrip() for line in file]

class BloomFilter:
    def __init__(self, m, k ):
        self.m = m #size of bloom filter
        self.k = k  #number of hash functions
        self.n = 0 #total count of the elements inserted in a set
        self.Table = [[]for i in range(self.m)]


    def might_contain(self, key):
        i = abs(hash(key) % len(self.TableGood))
        j = abs(hash(key) % len(self.TableBad))
       for i in self.Table(key):
           if self.

    def _true_bits(self):
        return 1

    def add(self, param):
        pass