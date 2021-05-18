def in_array(array1,array2):
    result = []
    for i in array2:
        for j in array1:
            if j in i and j not in result:
                result.append(j)
    return sorted(result)