def narcissistic(value):
    narcissistic_number = str(value)
    result = 0
    for number in narcissistic_number:
        result+=int(number)**len(narcissistic_number)
    return result