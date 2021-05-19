import re
from itertools import zip_longest


def abbreviate(s):
    split_alp = re.split('[^a-zA-Z]', s)
    split_symbol = re.findall('[^a-zA-Z ]', s)
    for i, j in zip_longest(split_alp, split_symbol):
        print(s.index(j))
    print(split_alp, split_symbol)


abbreviate("elephant-riders are really fun!")
