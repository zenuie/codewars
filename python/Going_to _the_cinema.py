import math


def movie(card, ticket, perc):
    num = 0
    price_a = 0
    price_b = card

    while math.ceil(price_b) >= price_a:
        num += 1
        price_a += ticket
        price_b += ticket * (perc ** num)
    return num
