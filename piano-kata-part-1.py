def black_or_white_key(key_press_count):
    key_press_count = key_press_count % 88
    if key_press_count in [0, 1, 3, 87]:
        return "white"
    elif key_press_count == 2:
        return "black"
    elif key_press_count >= 4 and key_press_count <= 8:
        if key_press_count % 2 == 0:
            return "white"
        else:
            return "black"
    elif key_press_count >= 9 and key_press_count <= 15:
        if key_press_count % 2 == 0:
            return "black"
        else:
            return "white"
    elif key_press_count > 15:
        key_press_count = key_press_count % 12
        if key_press_count in [1, 3, 87, 88]:
            return "white"
        elif key_press_count == 2:
            return "black"
        elif key_press_count >= 4 and key_press_count <= 8:
            if key_press_count % 2 == 0:
                return "white"
            else:
                return "black"
        elif key_press_count >= 9 and key_press_count <= 15:
            if key_press_count % 2 == 0:
                return "black"
            else:
                return "white"
        elif key_press_count == 0:
            return "black"