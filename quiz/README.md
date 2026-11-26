# 🎯 Python Quiz Application (v2 — OOP & JSON Persistence)

A modular, command-line quiz application built in Python 3 featuring categorized question decks, multiple-choice and typed questions, persistent multi-player statistics, and a targeted mistake-review mode.

## 📂 Project Structure

```text
quizz/
├── main.py          # Entry point, player login, main menu, and stats view
├── models.py        # Question, Deck, and QuizSession classes
├── storage.py       # JSON loading/saving for decks.json and progress.json
├── decks.json       # Categorized question decks (Python, DSA, DBMS)
├── progress.json    # Auto-generated player history and missed questions
└── README.md        # Project documentation
