def alphabet_position(text):
    result = ""
    text = ''.join(text).lower()  # 合併空格
    word_convert_num = {'a': '1 ', 'b': '2 ', 'c': '3 ', 'd': '4 ', 'e': '5 ', 'f': '6 ', 'g': '7 ', 'h': '8 ',
                        'i': '9 ', 'j': '10 ',
                        'k': '11 ', 'l': '12 ', 'm': '13 ', 'n': '14 ', 'o': '15 ', 'p': '16 ', 'q': '17 ', 'r': '18 ',
                        's': '19 ',
                        't': '20 ', 'u': '21 ', 'v': '22 ', 'w': '23 ', 'x': '24 ', 'y': '25 ', 'z': '26 ', '': ''}
    for word in text:
        if word.isalpha():
            result += word_convert_num[word]
    return result.strip()
