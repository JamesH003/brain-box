import random
import os
import time
from string import ascii_lowercase
from questions import QUESTIONS_CAPITALS, QUESTIONS_CURRENCIES

MAX_QUESTIONS = 10
CATEGORY = None
QUESTIONS = None
NAME = ""


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


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
        NAME = input("Please enter your name: ")

        if not NAME.isalpha() or len(NAME) < 2 or len(NAME) > 15:
            clear()
            print(f"{NAME} is an invalid name. Please type 2-15 letters.")
        else:
            break


def validate_category():
    """
    Ensure the user is selecting a valid category.
    """
    global CATEGORY

    time.sleep(0.5)
    print("Please choose a category: ")

    while True:
        category = input("1. Capitals \n2. Currencies\n")
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
            print(f"{category} is an invalid option. Please select 1 or 2.")


def loop_questions():
    """
    Main function loop
    """
    global QUESTIONS
    global NAME

    correct_answers = 0
    for num, (question, options) in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {num}:")
        correct_answers += show_next_question(question, options)
        # Gives the user control to move onto the next question
        # and clears previous question from terminal
        time.sleep(0.5)
        input("\nPress ENTER to continue\n")
        clear()

    # plural of questions or question depending on quantity of correct answers
    q = "question" if correct_answers == 1 else "questions"
    print(
        f"\nCongratulations {NAME}!! "
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
        again = input("Do you want to play again? (yes/no)\n").lower()
        clear()
        if again[0] == "y":
            print("... Loading Game ...")
            time.sleep(2)
            clear()
            launch_quiz()
            break
        elif again[0] == "n":
            print(f"Thanks for playing Brainbox {NAME}!")
            break
        else:
            print(f"{again} is not valid. Please type 'Y' or 'N'")


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
        print("\nCorrect! ✅")
        time.sleep(0.05)
        return True
    else:
        print(
            "\nWrong! ❌ "
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
    while (answer_label := input("\nAnswer? ").lower()) not in labeled_options:
        print(f"Please answer one of {', '.join(labeled_options)}")

    return labeled_options[answer_label]


# Calls welcome function
if __name__ == "__main__":
    clear()
    welcome()


# References
# https://www.geeksforgeeks.org/python-string-ascii_lowercase/
# https://realpython.com/python-enumerate/
# https://www.w3schools.com/python/ref_func_min.asp
# https://emojipedia.org/search/?q=flags
# https://www.w3schools.com/python/ref_random_choices.asp
# https://www.w3schools.com/python/ref_random_sample.asp