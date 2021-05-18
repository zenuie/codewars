def solution(s):
    ct = 2
    if s == "":
        return s
    elif len(s)%2 == 0:
        for i in range(len(s) // 2 - 1):
            s = list(s)
            s.insert(ct, "#")
            s = "".join(s)
            ct += 3
        return s.split("#")
    elif len(s)%2 !=0:
        for i in range(len(s) // 2):
            s = list(s)
            s.insert(ct, "#")
            ct += 3
            s = "".join(s)
        s = s+"_"
        s = s.split("#")
        return s