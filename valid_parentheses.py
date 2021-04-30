def valid_parentheses(string):
    count = 0
    for i in string:
        if count < 0:
            return False
        elif i == "(":
            count += 1
        elif i == ")":
            count -= 1

    if count == 0:
        return True
    else:
        return False
