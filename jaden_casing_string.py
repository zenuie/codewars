def to_jaden_case(string):
    result = ''
    string = string.split()
    for i in string:
        result += i.capitalize() + " "
    return result.strip()
