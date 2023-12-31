import random
import os
import time
import colorama
from colorama import Fore, Back, Style
from string import ascii_lowercase
from questions import QUESTIONS_CAPITALS, QUESTIONS_CURRENCIES

colorama.init(autoreset=True)

MAX_QUESTIONS = 10
CATEGORY = None
QUESTIONS = None
NAME = ""


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome():
    """
    Welcome message, name validation & starts quiz
    """
    global NAME

    print(f"{Fore.CYAN}{Style.BRIGHT} \nWelcome to Brainbox!\n")
    time.sleep(1)

    # get the user's name
    validate_name()
    clear()
    print(f"{Fore.YELLOW}{Style.BRIGHT}Welcome {NAME}!")

    # start the quiz
    launch_quiz()


def launch_quiz():
    """
    Starts the quiz
    """
    global CATEGORY
    global QUESTIONS

    # validate user category selection
    validate_category()

    # category_selection(selection)
    time.sleep(0.05)

    QUESTIONS = load_question_options(CATEGORY, MAX_QUESTIONS)
    time.sleep(0.05)
    # start the main function loop of questions
    loop_questions()


def validate_name():
    """
    Validate that the user's name is valid
    """
    global NAME

    while True:
        NAME = input(f"{Style.BRIGHT}Please enter your name: ")

        if not NAME.isalpha() or len(NAME) < 2 or len(NAME) > 15:
            clear()
            print(
                f"{Fore.RED}{Style.BRIGHT}{NAME!r} "
                "is an invalid name. Please type 2-15 letters.")
        else:
            break


def validate_category():
    """
    Ensure the user is selecting a valid category.
    """
    global CATEGORY

    time.sleep(0.5)
    print(f"{Style.BRIGHT}Please choose a category: ")

    while True:
        category = input(
            f"{Fore.GREEN}{Style.BRIGHT}"
            "1. Capitals \n2. Currencies\n")
        clear()

        if category == "1":
            # Capitals
            CATEGORY = QUESTIONS_CAPITALS
            break
        elif category == "2":
            # Currencies
            CATEGORY = QUESTIONS_CURRENCIES
            break
        else:
            print(
                f"{Fore.RED}{Style.BRIGHT}{category!r} "
                "is an invalid option. Please select 1 or 2.")


def loop_questions():
    """
    Main function loop
    """
    global QUESTIONS
    global NAME

    correct_answers = 0
    for num, (question, options) in enumerate(QUESTIONS, start=1):
        print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion {num}:")
        correct_answers += show_next_question(question, options)
        # Gives the user control to move onto the next question
        # and clears previous question from terminal
        time.sleep(0.5)
        input(f"{Fore.YELLOW}{Style.BRIGHT}\nPress ENTER to continue\n")
        clear()

    # plural of questions or question depending on quantity of correct answers
    q = "question" if correct_answers == 1 else "questions"
    print(
        f"{Fore.YELLOW}{Style.BRIGHT}\nCongratulations {NAME}!! "
        f"{Fore.MAGENTA}{Style.BRIGHT}"
        f"You got {correct_answers} {q} right out of {num}!\n"
    )
    time.sleep(0.05)

    # play again
    play_again()


def play_again():
    """
    Ask the user if they want to play again.
    """
    global NAME

    while True:
        again = input(
            f"{Fore.CYAN}{Style.BRIGHT}"
            "Do you want to play again? (yes/no)\n").lower()
        clear()
        if again[0] == "y":
            print(f"{Fore.YELLOW}{Style.BRIGHT}... Loading Game ...")
            time.sleep(2)
            clear()
            launch_quiz()
            break
        elif again[0] == "n":
            print(
                f"{Fore.CYAN}{Style.BRIGHT}"
                f"Thank you for playing Brainbox, {NAME}!")
            break
        else:
            print(
                f"{Fore.RED}{Style.BRIGHT}{again!r} "
                "is not valid. Please type 'Y' or 'N'")


def load_question_options(questions, max_questions):
    """
    Loads questions and returns random order
    """
    max_questions = min(max_questions, len(questions))
    return random.sample(list(questions.items()), k=max_questions)


def show_next_question(question, options):
    """
    Calls next question and verifies right or wrong user selection
    """
    correct_option = options[0]
    sorted_options = random.sample(options, k=len(options))
    # Verifies right or wrong user selection
    answer = get_user_selection(question, sorted_options)
    if answer == correct_option:
        print(f"{Fore.GREEN}{Style.BRIGHT}\nCorrect! ✅")
        time.sleep(0.05)
        return True
    else:
        print(
            f"{Fore.RED}{Style.BRIGHT}\nWrong! ❌ "
            f"{Fore.CYAN}{Style.BRIGHT} "
            f"The correct answer is {correct_option!r}, not {answer!r}"
        )
        time.sleep(0.05)
        return False


def get_user_selection(question, options):
    """
    Handles user input, labels options with ascii lowercase
    """
    print(f"{question}")
    labeled_options = dict(zip(ascii_lowercase, options))
    for label, option in labeled_options.items():
        print(f"  {label}) {option}")
    # Handles user errors
    while (
         answer_label := input(
              f"{Fore.CYAN}"
              f"{Style.BRIGHT}\nAnswer? ").lower()) not in labeled_options:
        print(
            f"{Fore.RED}{Style.BRIGHT}"
            f"Please answer one of {', '.join(labeled_options)}")

    return labeled_options[answer_label]


# Calls welcome function
if __name__ == "__main__":
    clear()
    welcome()
