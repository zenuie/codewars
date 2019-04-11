def rps(p1, p2):
    # your code here
    #     paper = 1
    #     rock = 2
    #     scissors = 3

    # "Player 1 won!"
    if p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"

    # "Player 2 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    else:
        return 'Draw!'