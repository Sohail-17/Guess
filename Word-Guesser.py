import random
import json
import os

FILE_NAME = "qa.json"  # combined questions + answers

# Load questions + answers safely
if os.path.exists(FILE_NAME):
    try:
        with open(FILE_NAME, "r") as f:
            qa_list = json.load(f)
            if not isinstance(qa_list, list):  # sanity check
                raise ValueError
    except (json.JSONDecodeError, ValueError):
        qa_list = [{"question": "Who's the smartest of them all?", "answer": "sohail"}]
else:
    qa_list = [{"question": "Who's the smartest of them all?", "answer": "sohail"}]

print("Welcome to the meme guesser!")

words = [qa["answer"].lower() for qa in qa_list]  # all answers for validation
word = random.choice(words)
guesses = max(1, len(word) // 2)
place_holder = "_" * len(word)

print(f"The word has {len(word)} letters and you have {guesses} attempts.")
print(f"{place_holder}")

# Let user add new question + answer pairs
while True:
    new_q = input("Add a question (or press Enter to stop): ").strip()
    if not new_q:
        break
    new_a = input("Answer for this question: ").strip().lower()
    if new_a:
        qa_list.append({"question": new_q, "answer": new_a})

# Save updated JSON back to file
with open(FILE_NAME, "w") as f:
    json.dump(qa_list, f, indent=2)

# Start guessing loop
while guesses > 0:
    qa = random.choice(qa_list)
    q = qa["question"]
    correct_answer = qa["answer"].lower()

    user_input = input(f"{q}: ").strip().lower()
    if user_input == correct_answer:
        print("Damn! You are the skibidi ohio rizzler bruh!")
        break
    else:
        guesses -= 1
        print(f"L bozo! You have {guesses} attempts left.")

if guesses == 0:
    print(f"Damn! No rizz for you hahahaaha! \nThe word was {word}.")