import random
from string import ascii_lowercase

QUESTION_QUANTITY_PER_GAME = 10
QUESTION_OPTIONS = {
    "What is the capital city of Portugal? 🇵🇹": [
        "Lisbon", "Caracas", "Faro", "Ottawa"
    ],
    "What is the capital city of Denmark? 🇩🇰": [
        "Copenhagen", "Moscow", "Tokyo", "Stockholm"
    ],
    "What is the capital city of Cuba? 🇨🇺": [
        "Havana", "Jakarta", "Cairo", "Miami"
    ],
    "What is the capital city of Argentina? 🇦🇷": [
        "Buenos Aires", "Budapest", "Monrovia", "Maseru"
    ],
    "What is the capital city of Croatia? 🇭🇷": [
        "Zagreb", "Accra", "Damascus", "Split"
    ],
    "What is the capital city of Lithuania? 🇱🇹": [
        "Vilnius", "Havana", "Budapest", "Prague"
    ],
    "What is the capital city of Indonesia? 🇮🇩": [
        "Jakarta", "Minsk", "Ankara", "Maputo"
    ],
    "What is the capital city of India? 🇮🇳": [
        "New Delhi", "Riyadh", "Manama", "Kuala Lumpur"
    ],
    "What is the capital city of Switzerland? 🇨🇭": [
        "Bern", "Zurich", "Belgrade", "Roseau" 
    ],
    "What is the capital city of Austria? 🇦🇹": [
        "Vienna", "Berlin", "Moroni", "Tallinn"
    ],
    "What is the capital city of Czech Republic? 🇨🇿": [
        "Prague", "Kuwait", "Tirana", "Dublin"
    ],
    "What is the capital city of Egypt? 🇪🇬": [
        "Cairo", "Madrid", "Rome", "Asmara"
    ],
    "What is the capital city of Barbados? 🇧🇧": [
        "Bridgetown", "Niamey", "Nassau", "Roseau"
    ],
    "What is the capital city of Sweden? 🇸🇪": [
        "Stockholm", "San Marino", "Oslo", "Valletta"
    ],
    "What is the capital city of Colombia? 🇨🇴": [
        "Bogota", "Brasilia", "Kingston", "Tehran"
    ],
    "What is the capital city of Greece? 🇬🇷": [
        "Athens", "Port-au-Prince", "Singapore", "Chișinău"
    ],
    "What is the capital city of Estonia? 🇪🇪": [
        "Tallinn", "Baghdad", "Lisbon", "Nursultan"
    ],
    "What is the capital city of Germany? 🇩🇪": [
        "Berlin", "Yaren district", "Munich", "Brussels"
    ],
     "What is the capital city of Slovakia? 🇸🇰": [
        "Bratislava", "Kyiv", "Bucharest", "Athens"
     ],
     "What is the capital city of Ireland? 🇮🇪": [
        "Dublin", "Cardiff", "Paris", "Cork"
     ]
}

quantity_questions = min(QUESTION_QUANTITY_PER_GAME, len(QUESTION_OPTIONS))
questions = random.sample(list(QUESTION_OPTIONS.items()), k=quantity_questions)

# correct_answers = 0
# for num, (question, options) in enumerate(questions, start=1):
#     print(f"\nQuestion {num}:")
#     print(f"{question}")
#     correct_option = options[0]
#     labeled_options = dict(
#         zip(ascii_lowercase, random.sample(options, k=len(options)))
#     )
#     for label, option in labeled_options.items():
#         print(f" {label}) {option}")

#     while (answer_label := input("\nAnswer? \n")) not in labeled_options:
#         print(f"Please answer one of {', '.join(labeled_options)}")

#     answer = labeled_options[answer_label]
#     if answer == correct_option:
#         correct_answers += 1
#         print("Correct! ✅")
#     else:
#         print(f"Wrong! ❌ The correct answer is {correct_option!r}")

# print(f"\nYou got {correct_answers} question(s) right out of {num}! ")


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

    # Result of game
    print(f"\nYou got {correct_answers} question(s) right out of {num}! ")

def load_question_options(questions, quantity_questions):


def show_next_question(question, options):


def get_user_selection(question, options):





# References
# https://www.geeksforgeeks.org/python-string-ascii_lowercase/
# https://realpython.com/python-enumerate/
# https://www.w3schools.com/python/ref_func_min.asp
# https://emojipedia.org/search/?q=flags
# https://www.w3schools.com/python/ref_random_choices.asp
# https://www.w3schools.com/python/ref_random_sample.asp