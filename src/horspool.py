

class HorspoolStringMatcher:

    def __init__(self, pattern):
        self.pattern = pattern
        self.shift_table = {}
        self.create_shift_table()

    #creates a shift table that skips over parts of text
    def create_shift_table(self):
        m = len(self.pattern)
        # dis-include the 0th position
        for i in range(m - 1):
            #will skip over duplicates
            self.shift_table[self.pattern[i]] = m - 1 - i

        return self.shift_table

    #returns the shift val of that char
    def _get_shift(self, char):
        #returns the shift tables character and scope of pattern
        return self.shift_table.get(char, len(self.pattern))

    #matches the shift value of the pattern to the text
    def match(self, text):
        sp = len(self.pattern)
        st = len(text)

        i = sp - 1
        k = 0
        #moving from right to left
        #while the pattern is less than the text string
        while i < st:
            k = 0
            #while the index is less than the pattern and the
            #pattern[scope of pattern -1 - index] is == to the text[pattern - index]
            while k < sp and self.pattern[sp - 1 - k] == text[i - k]:
                #iterate up
                k += 1
            #if the index is equal to the scope of pattern
            if k == sp:
                #return the position of match
                return i - sp + 1
            else:
                #else move around in the shift table
                i+= self.shift_table.get(text[i], sp)
        #no match return -1
        return -1



#pattern = HorspoolStringMatcher('How much wood would a woodchuck chuck if a woodchuck could chuck wood?')
#print(pattern.shift_table)
#print(pattern._get_shift('How'))
#print(pattern.match('How'))

