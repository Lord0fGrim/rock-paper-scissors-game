##this is the rock paper scissors game
import random


def game():
    question = (input("Do you want to play a game?(yes/no) "))
    if question == "yes":
        p1 = input("rock/paper/scissors? ").capitalize()
        ai = ["rock","paper","scissors"]
        random_ai = random.choice(ai).capitalize()
        print("Player: " + p1)
        print("Computer: " + random_ai)
        if (p1 == random_ai):
            print("Draw")
        # python if condition is true, result to be win
        elif(p1 == "Rock" and random_ai == "Scissors") or (p1 == "Paper" and random_ai == "Rock") or (p1 =="Scissors" and random_ai =="Paper"):
            print("Player Wins!")
        # python else statement, result to be lose
        else:
            print("A.I. Wins!")
        return game()
    elif question == "no":
        print("Go eat shit!!!")
        return game()







