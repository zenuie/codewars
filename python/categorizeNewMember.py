def openOrSenior(data):
    dataList = []
    for i in data:
        if i[0] >= 55 and i[1] >= 7:
            dataList.append("Senior")
        else:
            dataList.append("Open")
    return dataList


openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]])