# Random Number Generator in Python using the Random Standard Library
import random
print("\nWelcome! \n\n")
mode = input("Choose a mode: ")
if mode == 'AI':
    choose = int(input("Choose a number 1-10: "))
    if choose > 10:
        print("Invalid!")
        quit()
    print("Your number: \n")
    print(choose)

    opponent = random.randint(1,10)
    print("Opponent's number: \n")
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
    print(name1 + "'s number: \n")
    print(player1)
    print(name2 + "'s number: \n")
    print(player2)
    if player1 > player2:
        print(name1 + " wins!")

    if player1 < player2:
        print(name2 + " wins! ")



    if player1 == player2:
        print("Tie!")
if mode == 'randomized':
    choice = input("Do you want to play against the computer or a friend?: ")

    if choice == 'computer':
        computer = int(random.randint(1,10))
        player = int(random.randint(1,10))
        print("Your Number: \n")
        print(player)
        print("Opponent's Number: \n")
        print(computer)
        if computer > player:
            print("computer wins!")
        if computer < player:
            print("you win!")

        if computer == player:
            print("tie!")
    if choice == 'friend':
        player_name1 = input("What is your name, player 1?: ")
        player_name2  =input("What is your name, player 2?: ")
        player1number = random.randint(1,10)
        player2number = random.randint(1,10)

        print(player_name1 + "'s number is: \n")
        print(player1number)
        print(player_name2 + "'s number is: \n")
        print(player2number)

        if player1number > player2number:
            print(player_name1 + " wins!")

        if player1number < player2number:
            print(player_name2 + " wins!")

        if player1number == player2number:
            print("Tie!")

        