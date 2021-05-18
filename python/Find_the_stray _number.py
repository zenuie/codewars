def stray(arr):
    global ans
    b = []
    for x in arr:
        if arr.count(x) == 1:
            b.append(x)
        for y in b:
            ans = y
    return ans
