import re


def unique_in_order(iterable):
    global reIterable
    newIterable = []
    listIterable = []
    count = 0
    num = 0
    iterable = [str(x) for x in iterable]
    for x in iterable:
        listIterable.append(x)
    if len(listIterable) == 1 or len(listIterable) == 0:
        return listIterable
    elif listIterable[0] != listIterable[1]:
        newIterable.append(listIterable[0])
    for i in listIterable:
        count += 1
        if count < len(listIterable):
            for j in listIterable[count]:
                if i != j:
                    newIterable.append(j)
                    num += 1
                elif i == j and num < 1:
                    num += 1
                    newIterable.append(i)
                reIterable = re.findall('[0-9]', j)
    if reIterable:
        newIterable = list(map(int, newIterable))
    return newIterable
