def getCount(inputStr):
    num_vowels = 0
    # your code here
    inputStr.lower()
    for i in inputStr:
        if i == "a":
            num_vowels+=1
        elif i == "e":
            num_vowels+=1
        elif i == "i":
            num_vowels+=1
        elif i == "o":
            num_vowels+=1
        elif i == "u":
            num_vowels+=1

    return num_vowels