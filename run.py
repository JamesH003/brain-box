import random
import os
from string import ascii_lowercase

MAX_QUESTIONS = 10
CATEGORY = None
QUESTIONS = None
NAME = ""


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


    global CATEGORY
    global QUESTIONS
    """
    Welcome message, name validation & starts quiz
    """
    global NAME

    print("\nWelcome to Brainbox!\n")
    time.sleep(1)

    # get the user's name
    validate_name()
    clear()
    print(f"Welcome {NAME}!")

    # start the quiz
    launch_quiz()


def launch_quiz():
    # Loads questions
    questions = load_question_options(
        QUESTION_OPTIONS, quantity_questions=QUESTION_QUANTITY_PER_GAME
    )

    # Main function loop
    correct_answers = 0
    for num, (question, options) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        correct_answers += show_next_question(question, options)
        input("\nPress ENTER to continue\n")
        clear()

    # Result of game
    print(f"\nYou got {correct_answers} question(s) right out of {num}! ")


# Loads questions
def load_question_options(questions, quantity_questions):
    quantity_questions = min(quantity_questions, len(questions))
    return random.sample(list(questions.items()), k=quantity_questions)


# Calls next question and verifies right or wrong user selection
def show_next_question(question, options):
    correct_option = options[0]
    sorted_options = random.sample(options, k=len(options))
    # Verifies right or wrong user selection
    answer = get_user_selection(question, sorted_options)
    if answer == correct_option:
        print("Correct! ✅")
        return True
    else:
        print(f"Wrong! ❌ The correct answer is {correct_option!r}, not {answer!r}")
        return False


# Handles user input
def get_user_selection(question, options):
    print(f"{question}?")
    labeled_options = dict(zip(ascii_lowercase, options))
    for label, option in labeled_options.items():
        print(f"  {label}) {option}")
    # Handles user errors
    while (answer_label := input("\nAnswer? ")) not in labeled_options:
        print(f"Please answer one of {', '.join(labeled_options)}")

    return labeled_options[answer_label]


# Defines clear function
def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


# Calls launch_quiz function
if __name__ == "__main__":
    launch_quiz()



# References
# https://www.geeksforgeeks.org/python-string-ascii_lowercase/
# https://realpython.com/python-enumerate/
# https://www.w3schools.com/python/ref_func_min.asp
# https://emojipedia.org/search/?q=flags
# https://www.w3schools.com/python/ref_random_choices.asp
# https://www.w3schools.com/python/ref_random_sample.asp