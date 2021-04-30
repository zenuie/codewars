def iq_test(number):
    countOdd = 0
    countEven = 0
    odd = 0
    even = 0

    number = number.split()  # 先切片
    for i in number:
        if int(i) % 2 == 0:
            countOdd += 1
            odd += int(i)
        else:
            even += int(i)
            countEven += 1
    if countEven > countOdd:
        oddAns = number.index(str(odd))
        return oddAns + 1
    else:
        evenAns = number.index(str(even))
        return evenAns + 1


iq_test("2 4 7 8 10")