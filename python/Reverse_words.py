def reverse_words(text):
# go for it
    return " ".join(text[::-1].split(" ")[::-1])




reverse_words('The quick brown fox jumps over the lazy dog.')
reverse_words('apple')
reverse_words('a b c d')
reverse_words('double  spaced  words')