from functions import clear_console, right_answer_string_options
from data import options
import random


def game():

    user_score = 0
    computer_score = 0

    while True:
        
        user_option = right_answer_string_options("What do you choose? Rock, Paper or Scissors.\n", ["r","p","s"])

        if user_option == "r":
            user_choice = 0
        elif user_option  == "p":
            user_choice = 1
        else:
            user_choice = 2

        print(options[user_choice])
        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(options[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
            user_score += 1
        elif user_choice == 2 and computer_choice == 0:
            print("You lose!")
            computer_score += 1
        elif user_choice > computer_choice:
            print("You win!")
            user_score += 1 
        elif user_choice < computer_choice:
            print("You lose!")
            computer_score += 1
        else:
            print("It's a draw!")

        status = right_answer_string_options("would you like to continue?\n", ["y", "n"])

        clear_console()
        if status == "n":
            print(f"Final Score - You: {user_score}     Computer: {computer_score}")
            break
        else: 
            print(f"Current Score - You: {user_score}   Computer: {computer_score}")


clear_console()
game()