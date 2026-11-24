"""
Interactive Quiz Game
---------------------
A beginner-friendly command-line quiz application that reads questions from a
text file, shuffles them, evaluates user input, and shows a detailed score report.
"""

import os
import random


def load_questions(path):
    """
    Reads a file with questions in the format 'question|answer(s)',
    where multiple accepted answers can be separated by commas (stretch goal).
    Returns a list of dictionaries for each valid question.
    Skips blank lines and lines without '|' without crashing.
    """
    if not os.path.exists(path):
        print(f"Error: Could not find '{path}'. Please check the file path.")
        return []

    questions = []
    with open(path, "r", encoding="utf-8") as file:
        for line_number, raw_line in enumerate(file, start=1):
            line = raw_line.strip()

            # Skip blank or whitespace-only lines
            if not line:
                continue

            # Ensure the line contains the pipe separator '|'
            if "|" not in line:
                print(f"[Warning] Line {line_number} skipped (missing '|'): {line}")
                continue

            # Split question and answers on the first '|'
            parts = line.split("|", 1)
            question_text = parts[0].strip()
            answer_part = parts[1].strip()

            if not question_text or not answer_part:
                print(f"[Warning] Line {line_number} skipped (empty question or answer): {line}")
                continue

            # Support stretch goal: multiple accepted answers separated by commas
            # Compare answers fairly using .strip().lower() on both sides
            accepted_answers = [
                ans.strip().lower()
                for ans in answer_part.split(",")
                if ans.strip()
            ]

            questions.append({
                "question": question_text,
                "display_answer": answer_part,
                "accepted_answers": accepted_answers
            })

    return questions


def ask_question(q, question_num=None, total_questions=None):
    """
    Prints the question, reads the user's answer, and returns True or False.
    Compares answers using .strip().lower() on both sides.
    Also records the user's raw response in q['user_answer'] for end-of-game review.
    """
    if question_num is not None and total_questions is not None:
        print(f"\nQuestion {question_num}/{total_questions}:")
    else:
        print("\nQuestion:")

    print(f"  {q['question']}")

    user_input = input("  Your answer: ")
    normalized_input = user_input.strip().lower()
    q["user_answer"] = user_input.strip()

    if normalized_input in q["accepted_answers"]:
        print("  [+] Correct! Great job!")
        return True
    else:
        print(f"  [-] Incorrect. The correct answer was: {q['display_answer']}")
        return False


def get_question_count(max_available):
    """
    Prompts the user to choose how many questions they want to attempt,
    validating input to ensure it falls within [1, max_available].
    """
    while True:
        choice = input(f"How many questions would you like to answer? (1-{max_available}): ").strip()
        if choice.isdigit():
            count = int(choice)
            if 1 <= count <= max_available:
                return count
        print(f"Please enter a valid number between 1 and {max_available}.")


def run_quiz(questions):
    """
    Runs one round of the quiz game:
    - Shuffles the question list using random.shuffle
    - Asks the chosen number of questions
    - Calculates score, percentage, and lists incorrect questions
    """
    # Create a fresh copy and shuffle so original order isn't permanently altered
    shuffled_questions = list(questions)
    random.shuffle(shuffled_questions)

    total_available = len(shuffled_questions)
    num_to_ask = get_question_count(total_available)

    score = 0
    incorrect_records = []

    print("\n" + "=" * 50)
    print("               STARTING THE QUIZ!                 ")
    print("=" * 50)

    for i in range(num_to_ask):
        current_q = shuffled_questions[i]
        is_correct = ask_question(current_q, i + 1, num_to_ask)

        if is_correct:
            score += 1
        else:
            user_ans = current_q.get("user_answer", "")
            incorrect_records.append({
                "question": current_q["question"],
                "user_answer": user_ans if user_ans else "(No answer)",
                "correct_answer": current_q["display_answer"]
            })

    # Summary and score calculation
    percentage = (score / num_to_ask) * 100

    print("\n" + "=" * 50)
    print("                   QUIZ RESULTS                   ")
    print("=" * 50)
    print(f"Final Score: {score} / {num_to_ask}")
    print(f"Percentage : {percentage:.1f}%")

    if score == num_to_ask:
        print("\nOutstanding! Perfect score! 🌟")
    elif percentage >= 70:
        print("\nWell done! Solid performance! 👍")
    else:
        print("\nGood effort! Review the questions below to improve. 💡")

    # Review missed questions
    if incorrect_records:
        print("\n--- Questions to Review ---")
        for idx, item in enumerate(incorrect_records, start=1):
            print(f"\n{idx}. {item['question']}")
            print(f"   Your answer   : {item['user_answer']}")
            print(f"   Correct answer: {item['correct_answer']}")
    else:
        print("\nYou answered every question correctly!")

    print("=" * 50)


def main():
    """
    Main entry point for the Quiz Game.
    Loads questions from 'questions.txt' and handles the 'Play again? (y/n)' loop.
    """
    questions_file = "questions.txt"

    print("=" * 50)
    print("          WELCOME TO THE PYTHON QUIZ GAME!        ")
    print("=" * 50)

    questions = load_questions(questions_file)

    if not questions:
        print("No questions could be loaded. Please check your questions file and try again.")
        return

    print(f"Successfully loaded {len(questions)} questions from '{questions_file}'.\n")

    # Outer replay loop
    while True:
        run_quiz(questions)

        # Prompt to play again
        while True:
            play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
            if play_again in ["y", "yes"]:
                print("\nRestarting quiz...\n")
                break
            elif play_again in ["n", "no"]:
                print("\nThank you for playing! Goodbye! 👋\n")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()
