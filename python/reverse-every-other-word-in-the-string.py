def reverse_alternate(string):
    count = 0
    str = ""
    str_list = string.split(" ")
    for i in str_list:
        count += 1
        if i == '':
            count -= 1
            pass
        if count % 2 == 0 and i != '':
            i = i.lstrip()
            str += " " + i[::-1] + " "

        elif count % 2 == 1:
            str += i
    return str.strip()