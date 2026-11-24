# Interactive Python Quiz Game

A modular command-line quiz application written in Python. This project demonstrates core programming fundamentals: file I/O, loops, conditional logic, functions, collections (lists and dictionaries), string manipulation, and user input validation.

---

## 📁 Project Structure

```text
.
├── questions.txt    # Question bank formatted as question|answer
├── quiz.py          # Main application code
└── README.md        # Documentation and walkthrough
```

---

## 🚀 How to Run

1. Open your terminal or command prompt in this directory (`e:/ag intern`).
2. Run the game using Python:

```bash
python quiz.py
```

---

## 🛠️ Features & Implementation Highlights

- **Robust File Parsing (`load_questions`)**:
  - Reads `questions.txt` line by line.
  - Skips empty lines and lines without a `|` separator without crashing.
  - Strips leading and trailing whitespace to prevent newline characters from corrupting questions and answers.
- **Fair Case-Insensitive Matching**:
  - Normalizes both the user's input and expected answers with `.strip().lower()`.
  - Entries like `Paris`, `paris`, and `  PARIS  ` are all evaluated as correct.
- **Stretch Goal: Multiple Accepted Answers**:
  - Supports alternative comma-separated answers on the same line (e.g., `What is the standard file extension for Python script files?|.py,py`).
- **Dynamic Question Count & Shuffling**:
  - Uses `random.shuffle()` to randomize the question order on each run.
  - Prompts the player to select how many questions they want to tackle (with numerical bounds validation).
- **Comprehensive Score Report & Review**:
  - Displays total score and percentage (e.g., `80.0%`).
  - Summarizes incorrect questions, detailing the question asked, what you entered, and the correct answer.
- **Replay Loop**:
  - Prompts the user with `Play again? (y/n)` to easily restart without restarting the script.

---

## 📝 Customizing `questions.txt`

You can customize or add new questions anytime. Follow this syntax:

```text
Your Question Here?|AcceptedAnswer1,AcceptedAnswer2
```

Example:
```text
What is the standard file extension for Python script files?|.py,py
Which data type is immutable: list or tuple?|tuple
```
