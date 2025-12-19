import os

def clear_console():
    """Clear the console based on the operating system(for better readability)"""
    os.system('cls' if os.name == 'nt' else 'clear')


def right_answer_string_options(user_question, list_of_options):
    """Prompts the user for a choice until a valid option is entered."""

    while True:
        user_choice = input(user_question).lower()

        if user_choice[0] in list_of_options:
            return user_choice[0]
        else:
            print("This option is not available. Please enter a suitable one.")