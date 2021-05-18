import re
def kebabize(string):
    string = re.sub(r'[^a-z,A-Z]',"",string)
    string = re.sub('[A-Z]', lambda x: "-" + x.group(0), string)
    string = string.strip("-")
    string = string.lower()
    return string















kebabize('myCamelCasedString')
kebabize('myCamelHas3Humps')
kebabize('SOS')
kebabize('42')
kebabize('CodeWars')