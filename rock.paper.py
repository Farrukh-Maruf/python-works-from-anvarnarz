# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:09:30 2022

@author: qomon
"""

import random
# it is a random function in order to randomly chose the action from the list

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

# Here a user enters his/her choice from the given options that are similar with the "[list]".
# After a choice of a user computer will randomly choose the options from the list.
# Then there will appear information of both sides choice.

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
# Here, if the choice of both a user and computer are equil, there will be printed a notification.


# From this positon there were looked every posibble action of a user and computer and by considering their action there were written some announcements.

    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
# Until here we have looked every possible choice

# After every attempt a user will automatically be asked whether he/she wants to continue or not. He/she chooses "y", a user will be returned to the beginning of the program, if no, the program will break the process. 
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
