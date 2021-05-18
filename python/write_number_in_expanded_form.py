def expanded_form(num):
    num = list(str(num))
    result = ''
    ct = len(num) - 1
    ct2 = 0
    for i in num:
        if int(i) != 0:
            position = num.index(i,ct2)
            result += i + '0' * (ct-position) + " " + "+" + " " #ct-position = digits
        ct2+=1
    return result[:-3]