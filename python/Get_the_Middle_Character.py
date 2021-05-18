def get_middle(s):
    # your code here
    if len(s) % 2 == 0:
        return s[len(s) / 2 - 1] + s[len(s) / 2]
    else:
        return s[len(s) / 2]
