def is_prime(num):
    #my_version
    #timeout
    #---------------------------------------
    # i = 3
    # if num ==2:
    #     return True
    # if num <=1 or num%2==0:
    #     return False
    # if i * i <= num:
    #     for x in range(i,num,2):
    #         if num%x == 0:
    #             return  False
    # return True
    #---------------------------------------
    if num <= 0 or num == 1:
        return False
    i = 2
    while (i <= num ** 0.5):
        if num % i == 0:
            return False
        i += 1
    return True