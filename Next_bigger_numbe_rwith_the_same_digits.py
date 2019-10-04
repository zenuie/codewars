def next_bigger(n):
    N = str(n)  # 轉字串方便運作
    N = list(N)
    revrN = N[::-1]  # 反轉，為了由後往前讀取
    nextNumber = 0
    lastNumberIndex = 0  # 記最後的數字位置
    delLastNumber = 0
    sortLastList = []
    for i in revrN:
        if int(i) >= nextNumber:  # 判斷後面的數字有沒有大於前面
            nextNumber = int(i)
            lastNumberIndex += 1
        else:
            sortLastList = sorted(revrN[0:lastNumberIndex])
            for j in sortLastList:
                if j > revrN[lastNumberIndex]:
                    revrN.insert(lastNumberIndex + 1, j)
                    sortLastList.append(revrN[lastNumberIndex])
                    del revrN[delLastNumber]
                    del sortLastList[delLastNumber]
                    sortLastList = sorted(revrN[0:lastNumberIndex])
                    break
                else:
                    delLastNumber += 1
            del revrN[0:lastNumberIndex]
            revrN = revrN[::-1]  # 反轉正常
            sorted(sortLastList)
            sortLastList = revrN.extend(sortLastList)
            revrN = '%s' * len(revrN) % tuple(revrN)
            return int(revrN)
    else:
        return -1
