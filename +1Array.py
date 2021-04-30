def up_array(arr):
    global total
    total = ""
    for i in arr:
        if i < 0 or i > 9:
            return None
        else:
            i = str(i)
            total += i
    if total == "":
        return None
    total = eval(total)
    total = total + 1
    total = list(str(total))
    total = list(map(int, total))
    return total
