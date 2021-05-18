def find_outlier(integers):
    odd = 0
    even = 0
    ct1 = 0
    ct2 = 0
    for i in integers:
        if i % 2 == 0:
            odd += i
            ct1 += 1
        else:
            even += i
            ct2 += 1
    return odd if ct2 > 1 else even
