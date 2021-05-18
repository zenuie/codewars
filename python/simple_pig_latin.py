def pig_it(text):
    result = []
    text = text.split()
    for i in text:
        if not i.isalpha():
            result.append(i)
            break
        i = list(i)
        i.append(i[0]+"ay")
        del i[0]
        result.append("".join(i))
    result = " ".join(result)
    print(result)