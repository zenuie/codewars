def printer_error(s):
    ct_error = 0
    words = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    for i in s:
        if i not in words:
            ct_error+=1
    return '{}/{}'.format(ct_error, len(s))