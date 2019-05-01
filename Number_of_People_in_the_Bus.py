def number(bus_stops):
    # Good Luck!
    # up
    # down
    # bus_stops->list轉int 取第一數相加後減第二數
    total = 0
    for i in bus_stops:
        sum = i[0]-i[1]
        total += sum
    print(total)
    print(type(total))













number([[10,0],[3,5],[5,8]])