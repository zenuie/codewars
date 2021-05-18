def find_uniq(arr):
    if arr[0]!=arr[1] and arr[0]!=arr[2]:
        return arr[0]
    for i in arr[1:]:
        if arr[0] != i:
            return i
        else:
            continue