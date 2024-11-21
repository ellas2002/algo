def str_match(text, pattern):
    for i in range(len(text)):
        if text[i:len(pattern) + i] == pattern:
            return i
    return -1

def str_find(text, pattern):
    for i in range(len(text)):
        if pattern != text:
            i = i + 1
        else:
            i
    return -1