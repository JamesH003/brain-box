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
    for option in sorted(options):
        print(f"  - {option}")

    answer = input(f"{question}? ")
    if answer == correct_option:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_option!r}")

