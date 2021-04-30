def likes(names):
    ct = len(names)
    if ct < 1:
        return 'no one likes this'
    elif ct == 1:
        return '{} likes this'.format(names)
    elif ct == 2:
        return '{} and {} like this'.format(names[0], names[1])
    elif ct == 3:
        return '{}, {} and {} like this'.format(names[0],names[1],names[2])
    elif ct > 3:
        return '{}, {} and {} others like this'.format(names[0],names[1],ct-2)