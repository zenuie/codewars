def tower_builder(n_floors):
    tower = []
    floor = ""
    result = []
    for f in range(n_floors):
        stars = '*' * (f * 2 + 1)
        space = ' ' * (n_floors - f - 1)
        floor = space + stars + space
        result.append(floor)

    return result