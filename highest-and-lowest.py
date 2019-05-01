def high_and_low(numbers):
    newNumber = numbers.split(" ")
    newNumber = list(map(int, newNumber))
    bnewNumber = str(max(newNumber))
    snewNumber = str(min(newNumber))
    newNumber = bnewNumber+" "+snewNumber
    return newNumber
