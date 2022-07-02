# Random Number Generator in Python using the Random Standard Library
import random
mode = input("Choose a mode, multiplayer or AI: ")
if mode == 'AI':
    choose = int(input("Choose a number 1-10: "))
    if choose > 10:
        print("Invalid!")
        quit()
    print(choose)

    opponent = random.randint(1,10)
    print(int(opponent))

    if opponent > choose: 
        print("You lost! ")
    if opponent < choose:
        print("You won! ")
    if opponent == choose:
        print("Tie!")

if mode == 'multiplayer':
    name1 = input("What is your name, Player 1?: ")
    name2 = input("What is your name, Player 2?: ")
    player1 = int(input(name1 + " choose a number 1-10: "))
    if player1 > 10:
        print("Invalid!")
        quit()
    player2 = int(input(name2 + " choose a number 1-10: "))
    if player2 > 10:
        print("Invalid!")
        quit()

    if player1 > player2:
        print(name1 + " wins!")

    if player1 < player2:
        print(name2 + " wins! ")



    if player1 == player2:
        print("Tie!")
