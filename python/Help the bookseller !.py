def stock_list(listOfArt, listOfCat):
    result = ""
    num_add = 0
    ct = 0
    for letter in listOfCat:
        for num in listOfArt:
            num = num.split(" ")
            if letter == num[0][0]:
                num_add += int(num[1])
            else:
                ct += 1
        result += "({} : {}) - ".format(letter, num_add)
        num_add = 0
    if ct == len(listOfCat) * len(listOfArt):
        return ''
    return result[:-3]


stock_list(listOfArt=["ABAR 200", "CDXE 500"]
           , listOfCat=["B", "R", "D", "X", "Z"])
