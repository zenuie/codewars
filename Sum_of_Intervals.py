def sum_of_intervals(intervals):
    splitInp = sorted(intervals)
    match = []
    for i in splitInp:
        for j in range(i[0], i[1]):
            match.append(j)
    return len(set(match))
