import re


def mix(s1, s2):
    result = []
    check_alp = '[a-z]'  # 正則
    s1 = re.findall(check_alp, s1)  # 小寫無重複
    s2 = re.findall(check_alp, s2)
    if s1 == s2:
        return ''
    dict_1 = dictS1(s1)  # 排出字典
    dict_2 = dictS2(s2)
    dict_1 = sorted(dict_1.items(), key=lambda x: (-x[1], x[0]))  # 字典值大的排前
    dict_2 = sorted(dict_2.items(), key=lambda x: (-x[1], x[0]))
    temp = ""
    print(dict_1)
    print(dict_2)
    for i in dict_1:
        for j in dict_2:
            if i[1] > j[1] and i[0] not in temp and j[0] not in temp:
                result.append("1:{}/".format(i[0] * int(i[1])))
                temp += i[0]
            elif i[1] < j[1] and i[0] not in temp and j[0] not in temp or i[0] != j[0] and i[1] == j[1] and j[0] not in temp:
                result.append("2:{}/".format(j[0] * int(j[1])))
                temp += j[0]
            elif i[0] == j[0] and i[1] == j[1]:
                result.append("=:{}/".format(j[0] * int(j[1])))
                temp += i[0]
        if i[0] not in temp:
            result.append("1:{}/".format(i[0] * int(i[1])))
            temp += i[0]
        
    print(result)


def dictS1(s1):
    dict_s1 = {}
    for i in set(s1):
        if s1.count(i) > 1:
            dict_s1["{}".format(i)] = s1.count(i)
    return dict_s1


def dictS2(s2):
    dict_s2 = {}
    for j in set(s2):
        if s2.count(j) > 1:
            dict_s2["{}".format(j)] = s2.count(j)
    return dict_s2


mix("A generation must confront the looming ", "codewarrs")
