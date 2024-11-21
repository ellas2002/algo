import fractions
class Fraction:

    def __init__(self, numerator, denominator):
        "denominator that is 0 is undefiined"
        if denominator == 0:
            print("denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        "uses gcd to reduce fraction"
        self.reduce()

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    @staticmethod
    def gcd(a, b):
        "from class"
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def reduce(self):
        "reduces fraction"
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd
        "if denominator is negative, give to numerator"
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        "isinstance checks to make sure self is a Fraction"
        if isinstance(other, Fraction):
            common_denominator = self.denominator * other.denominator
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            return Fraction(new_numerator, common_denominator)
        "if self is not a fraction..."
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            common_denominator = self.denominator * other.denominator
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            return Fraction(new_numerator, common_denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            common_denominator = self.denominator * other.denominator
            new_numerator = self.numerator * other.numerator
            return Fraction(new_numerator, common_denominator)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator or self.numerator == 0:
                print("undefined")
            common_denominator = self.denominator * other.numerator
            new_numerator = self.numerator * other.denominator
            return Fraction(new_numerator, common_denominator)
        return NotImplemented

    def __float__(self):
            return self.numerator / self.denominator
