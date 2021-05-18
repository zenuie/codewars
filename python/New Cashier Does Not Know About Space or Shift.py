def get_order(order):
    conver_to_can_sorted = ""
    result = ""
    cut_list = [6, 5, 7, 5, 8, 10, 9, 4]
    ct = len(order)
    meals = {
        "burger": "1",
        "fries": "2",
        "chicken": "3",
        "pizza": "4",
        "sandwich": "5",
        "onionrings": "6",
        "milkshake": "7",
        "coke": "8",
    }

    sorted_order = {
        "1":"Burger",
        "2":"Fries",
        "3":"Chicken",
        "4":"Pizza",
        "5":"Sandwich",
        "6":"Onionrings",
        "7":"Milkshake",
        "8":"Coke"
    }

    while ct > 0:
        for order_String in cut_list:
            if order[0:order_String] in meals:
                conver_to_can_sorted += meals[order[0:order_String]]
                order = order[order_String:]
        ct = len(order)

    for i in sorted(conver_to_can_sorted):
        result+=sorted_order[i]+" "
    return result.strip()


get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")
