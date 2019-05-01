import re


def reverse_letter(string):
    # do your magic here
    return re.sub(r'[^a-zA-Z]', "", string)[::-1]
