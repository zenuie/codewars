def high_and_low(numbers):

    numbers = numbers.split(" ")
    results = sorted(list(map(int,numbers)))
    return str(max(results))+" "+str(min(results))