def who_eats_who(zoo):
    eats = {"antelope": ["grass"],
            "big-fish": ["little-fish"],
            "bug": ["leaves"],
            "bear": ["big-fish", "bug", "chicken", "cow", "leaves", "sheep"],
            "chicken": ["bug"],
            "cow": ["grass"],
            "fox": ["chicken", "sheep"],
            "giraffe": ["leaves"],
            "lion": ["antelope", "cow"],
            "panda": ["leaves"],
            "sheep": ["grass"],
            "grass": [],
            "leaves": [],
            "little-fish": [],
            "tree": [],
            "banana": [],
            "bicycle": [],
            "busker": []}
    zoo_lst = zoo.split(",")
    out_lst = [zoo]
    count = 0
    while len(zoo_lst) != 1 and count < 100:
        for i in range(len(zoo_lst)):
            # This checks to see if they can eat whats on their left
            if i != 0 and zoo_lst[i - 1] in eats[zoo_lst[i]]:
                out_lst.append("{} eats {}".format(zoo_lst[i], zoo_lst[i - 1]))
                zoo_lst.pop(i - 1)
                break
            # This checks to see if they can eat whats on their right
            elif i != (len(zoo_lst) - 1) and zoo_lst[i + 1] in eats[zoo_lst[i]]:
                out_lst.append("{} eats {}".format(zoo_lst[i], zoo_lst[i + 1]))
                zoo_lst.pop(i + 1)
                break
        count += 1
    out_lst.append(",".join(zoo_lst))
    return out_lst
