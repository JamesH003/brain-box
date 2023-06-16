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
    ]
}

quantity_questions = min(QUESTION_QUANTITY_PER_GAME, len(QUESTION_OPTIONS))
questions = random.sample(list(QUESTION_OPTIONS.items()), k=quantity_questions)

correct_answers = 0
for num, (question, options) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}")
    correct_option = options[0]
    labeled_options = dict(
        zip(ascii_lowercase, random.sample(options, k=len(options)))
    )
    for label, option in labeled_options.items():
        print(f" {label}) {option}")

    while (answer_label := input("\nAnswer? ")) not in labeled_options:
        print(f"Please answer one of {', '.join(labeled_options)}")

    answer = labeled_options[answer_label]
    if answer == correct_option:
        correct_answers += 1
        print("Correct! ✅")
    else:
        print(f"Wrong! ❌ The correct answer is {correct_option!r}")

print(f"\nYou got {correct_answers} question(s) right out of {num}! ")

