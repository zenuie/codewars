def anagrams(word,words):
    result = []
    base = sorted(word)
    for i in words:
        if base == sorted(i):
            result.append(i)
    return result