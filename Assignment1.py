# Step 1: Setup (Questions Data)
quiz = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kano", "D. Ibadan"],
        "correct_answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "correct_answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "correct_answer": "C"
    }
]

# Step 2: Initialize score
score = 0

# Step 3: Loop through questions
for i, q in enumerate(quiz, start=1):
    print(f"\nQuestion {i}: {q['question']}")
    
    for option in q["options"]:
        print(option)
    
    # Step 4: Take user input
    answer = input("Your answer (A/B/C/D): ").upper()
    
    # Step 5: Check answer
    if answer == q["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['correct_answer']}")

# Step 6: Calculate percentage
def calculate_percentage(score, total):
    return (score / total) * 100

percentage = calculate_percentage(score, len(quiz))

# Step 7: Final Output
print("\n--- RESULT ---")
print(f"Score: {score}/{len(quiz)}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 50:
    print("PASS 🎉")
else:
    print("FAIL ❌")