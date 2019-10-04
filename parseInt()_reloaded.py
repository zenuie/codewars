def parse_int(string):
    strNumConvert = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6","seven": "7", "eight": "8", "nine": "9", "ten": "10",
                     "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17", "eighteen": "18","nineteen": "19",
                     "twenty": "20", "thirty": "30", "forty": "40", "fifty": "50", "sixty": "60", "seventy": "70", "eighty": "80","ninety": "90"}

    lst = string.split(" ")
    ans = ""
    for i in lst:
        if i in strNumConvert:
            ans += strNumConvert[i]
        elif "-" in i:
            i = i.split("-")
            temp = 0
            for j in i:
                temp += int(strNumConvert[j])
            ans += str(temp)
    return int(ans)







parse_int("one")