
def match(pattern, text):
    m = len(pattern)
    n = len(text)

    for i in range (n - m + 1):
        for j in range (n - m + 1):
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
