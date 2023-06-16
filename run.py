QUESTION_OPTIONS = {
    "What is the capital city of Portugal?": [
        "Lisbon", "Caracas", "Faro", "Ottawa"
    ],
    "What is the capital city of Denmark?": [
        "Copenhagen", "Moscow", "Tokyo", "Stockholm"
    ],
    "What is the capital city of Cuba?": [
        "Havana", "Jakarta", "Cairo", "Miami"
    ],
    "What is the capital city of Argentina?": [
        "Buenos Aires", "Budapest", "Monrovia", "Maseru"
    ],
    "What is the capital city of Croatia?": [
        "Zagreb", "Accra", "Damascus", "Split"
    ],
    "What is the capital city of Lithuania?": [
        "Vilnius", "Havana", "Budapest", "Prague"
    ],
    "What is the capital city of Indonesia?": [
        "Jakarta", "Minsk", "Ankara", "Maputo"
    ],
    "What is the capital city of India?": [
        "New Delhi", "Riyadh", "Manama", "Kuala Lumpur"
    ],
    "What is the capital city of Switzerland?": [
        "Bern", "Zurich", "Belgrade", "Roseau" 
    ],
    "What is the capital city of Austria?": [
        "Vienna", "Berlin", "Moroni", "Tallinn"
    ]
}

for question, options in QUESTION_OPTIONS.items():
    correct_option = options[0]
    sorted_options = sorted(options)
    for label, option in enumerate(sorted_options):
        print(f" {label}) {option}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_options[answer_label]
    if answer == correct_option:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_option!r}")


# for question, alternatives in QUESTIONS.items():
#     correct_answer = alternatives[0]
#     sorted_alternatives = sorted(alternatives)
#     for label, alternative in enumerate(sorted_alternatives):
#         print(f"  {label}) {alternative}")

#     answer_label = int(input(f"{question}? "))
#     answer = sorted_alternatives[answer_label]
#     if answer == correct_answer:
#         print("Correct!")
#     else:
#         print(f"The answer is {correct_answer!r}, not {answer!r}")
