def find_children(dancing_brigade):
    string1 = ""
    string = ""
    count = 0
    dancing_brigade = dancing_brigade.lower()
    dancing_brigade = sorted(dancing_brigade)

    for z in dancing_brigade:
        string1 += z
    dancing_brigade = string1.title()
    for h in dancing_brigade:
        if str(h).istitle():
            string += str(h).title()
        else:
            for i in dancing_brigade:
                count += 1
                if count < len(dancing_brigade):
                    for j in dancing_brigade[count]:
                        if i == j:
                            string += i
                        else:
                            if i.istitle():
                                string += j
                            else:
                                string += str(j).upper()
    return string
