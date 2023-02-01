computer = 'scissors'

player = input('Choose rock, paper or scissors: ')

if player == computer:
    print("DRAW")
elif player == 'paper':
    if computer == 'rock':
        print("YOU win")
    else:
        print("COMPUTER wins")
elif player == 'rock':
    if computer == 'scissors':
        print("YOU win")
    else:
        print("COMPUTER wins")
elif player == 'scissors':
    if computer == 'paper':
        print("YOU win")
    else:
        print("COMPUTER wins")
else:
    print("Fail!")
