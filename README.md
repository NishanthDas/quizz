# 🎯 Python Quiz Game

A simple, interactive command-line quiz game built using Python. The application reads questions from an external text file, presents them in a random order, checks user answers, and displays the final score.

This project was developed as a beginner-level Python project to practise programming fundamentals through a fun, interactive application.

## 📌 Project Overview

The Python Quiz Game allows users to:
- Answer multiple-choice-free, text-based quiz questions.
- Choose how many questions they want to attempt.
- Get questions in a randomized order.
- Receive instant feedback on their answers.
- View their final score and percentage.
- Review incorrect answers with their correct answers.
- Play multiple rounds without restarting the program.

## ✨ Features

- **File Handling:** Loads questions dynamically from `questions.txt`.
- **Randomized Questions:** Uses Python's `random` module to shuffle questions.
- **Flexible Answer Checking:** Ignores uppercase/lowercase differences and unnecessary spaces.
- **Score Calculation:** Displays the total correct answers and percentage.
- **Incorrect Answer Review:** Shows questions answered incorrectly along with their correct answers.
- **Replay Option:** Allows users to play again.
- **Input Validation:** Handles invalid inputs and skips improperly formatted question lines.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Modules:** `random`
- **Concepts:** 
  - File Handling
  - Lists and Dictionaries
  - Functions
  - Loops (`for` and `while`)
  - Conditional Statements
  - String Manipulation
  - Exception Handling

## 📂 Project Structure

```text
quiz/
│
├── quiz.py          # Main quiz application
├── questions.txt    # Quiz questions and answers
├── README.md        # Project documentation
└── T1 pics/         # Project screenshots
```

## 🚀 Getting Started

### 1. Prerequisites

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/NishanthDas/quizz.git
```

### 3. Navigate to the Project Folder

```bash
cd quizz
```

### 4. Run the Application

```bash
python quiz.py
```

## 📝 Questions File Format

The questions are stored in `questions.txt`.

Each line follows this format:

```text
What is the capital of France?|Paris
Which language is used for Python development?|Python
What is 5 + 5?|10
```

The question and answer are separated using a pipe (`|`) symbol.

You can customize the quiz by adding your own questions and answers to this file.

## 🎮 How to Play

1. Run the Python program.
2. Enter the number of questions you want to attempt.
3. Answer each question when prompted.
4. Receive feedback on your answers.
5. View your final score and percentage.
6. Review incorrect answers.
7. Choose whether to play another round.

## 🎓 Learning Outcomes

Through this project, I practised:

- Reading and processing external text files.
- Organizing data using Python lists and dictionaries.
- Creating reusable functions.
- Implementing loops and conditional logic.
- Working with randomization.
- Comparing strings efficiently.
- Handling user input and basic errors.

## 🔮 Future Improvements

Possible enhancements for future versions:

- Add multiple-choice questions.
- Introduce difficulty levels (Easy, Medium, Hard).
- Add a timer for each question.
- Implement a leaderboard and score history.
- Develop a graphical user interface (GUI).
- Add support for multiple quiz categories.

## 📸 Project Screenshots

Screenshots and demonstrations are available in the `T1 pics` folder.

## 👨‍💻 Author

**Nishanth Das**

GitHub: [@NishanthDas](https://github.com/NishanthDas)

---

⭐ If you find this project interesting, feel free to explore the code and experiment with your own quiz questions.

**Built with Python | Beginner Project | Learning by Building**
