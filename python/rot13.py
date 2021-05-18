def rot13(message):
    result = ""

    letter_dict = {
        " ": " ",
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    new_letter_dict = {v: k for k, v in letter_dict.items()}
    for letter in message:
        if not letter.isalpha():
            result += letter

        elif letter == letter.upper():
            letter = letter.lower()
            if letter_dict[letter] + 13 < 26:
                result += new_letter_dict[letter_dict[letter] + 13].upper()
            else:
                result += new_letter_dict[abs(26 - letter_dict[letter] - 13)].upper()

        else:
            if letter_dict[letter] + 13 <= 26:
                result += new_letter_dict[letter_dict[letter] + 13]
            else:
                result += new_letter_dict[abs(26 - letter_dict[letter] - 13)]
    return result
