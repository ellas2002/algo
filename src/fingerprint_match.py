def match(text, pattern):
    m = len(pattern)
    n = len(text)
    for i in range (n - m + 1):
        for j in range (n - m + 1):
            hash(x)
            hash(y)
            for x in range(m):
                for y in range(m):
                    if text[i + x][j + y] != pattern[x][y]:
                        break
                else:
                    continue
                break
            else:
                return i, j


    return None

#XOR OPERATION

a = 10  # 1010 in binary
b = 6   # 0110 in binary

result = a ^ b  # 1100 in binary

print(result)