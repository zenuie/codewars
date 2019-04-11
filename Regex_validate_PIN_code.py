import re


def validate_pin(pin):
    # return true or false
    if re.fullmatch("\d{4}|\d{6}", pin):
        return True
    else:
        return False
