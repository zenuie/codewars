def count(string):
    # The function code should be here
    dic = {}
    for i in string:
        dic[i] = string.count(i)
    return dic