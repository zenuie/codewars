import re


def increment_string(strng):
    condition_num = re.compile("[\d]+$")
    match_num = re.search(condition_num, strng)
    if not match_num:
        return strng + "1"
    elif strng == "":
        return "1"
    front = strng.replace(match_num.group(), "")
    end = str(int(match_num.group()) + 1).zfill(len(match_num.group()))

    return front + end
