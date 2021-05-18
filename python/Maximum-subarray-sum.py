def maxSequence(arr):
    maxSoFar = 0
    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum = sum + arr[j]
            maxSoFar = max(maxSoFar, sum)
    return maxSoFar
