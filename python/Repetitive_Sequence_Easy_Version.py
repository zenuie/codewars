def find(n):
    arr = [0, 1, 2, 2]
    if n <= 3:
        return arr[n]
    else:
        length = 4  # actual length of the array
        arr_sum = 5  # the total possible index with the current array
        for num in range(3, n + 1):
            arr_sum += arr[num] * num
            if arr_sum >= n:
                diff = (arr_sum - n) // num
                max_val = length - 1 + arr[num]
                return max_val - diff
            length += arr[num]
            if length < 100_000:
                arr.extend([num] * arr[num])


find(69)
