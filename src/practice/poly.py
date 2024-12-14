def poly(a, l):

    total = 0
    factor = 1
    for c in l:
        total += c * factor
        factor *= a

    return total

def horner(x, coefficients):
    if not coefficients:
        return 0
    return coefficients[0] + x * horner(x, coefficients[1:])

print(poly(3,[4,1,10]))
print(horner(3, [4,1,10]))