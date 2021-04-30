def spin_word(sentence):
    result = ""
    sentence = sentence.split()
    for i in sentence:
        if len(i) >=5:
            result+=i[::-1]+" "
        else:
            result+=i+" "
    return result.strip()