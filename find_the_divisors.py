def divisors(integer):
    result = []
    for i in range(2, integer):
        if integer % i == 0:
            result.append(i)
    if not result:
        return '{} is prime'.format(integer)
    return result
