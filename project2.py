import random

options = ('rock', 'paper', 'scissor')

player = input('Choose rock, paper or scissors: ').lower()

if player in options:
    computer = random.choice(options)

    print('Player option =>', player)
    print('CPU option =>', computer)

    if player == computer:
        print("DRAW")
    elif player == 'paper':
        if computer == 'rock':
            print("YOU win")
        else:
            print("COMPUTER wins")
    elif player == 'rock':
        if computer == 'scissor':
            print("YOU win")
        else:
            print("COMPUTER wins")
    else:
        if computer == 'paper':
            print("YOU win")
        else:
            print("COMPUTER wins")
else:
    print("Wrong")
