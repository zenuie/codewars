def is_pangram(s):
    check = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    a = []
    for i in s.lower():
        if i.isalpha():
            a.append(i)
    s_sort = sorted(set(a))
    # print(s_sort)
    return check == s_sort
