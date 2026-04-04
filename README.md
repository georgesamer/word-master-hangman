# Word Master Hangman

#### Video Demo: [YouTube URL HERE]

#### Description:

Word Master Hangman is a professional, CLI-based Hangman game developed as the final project for Harvard's CS50P (Introduction to Programming with Python). The game challenges players to guess a hidden English word, letter by letter, within a limited number of attempts — before the hangman figure is fully drawn.

The project goes beyond a basic Hangman implementation by focusing on code quality, offline reliability, user experience, and testability — all principles emphasized throughout CS50P.

---

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the game:
   ```
   python project.py
   ```
3. Run the tests:
   ```
   pytest test_project.py
   ```

---

## Key Features

**Offline Word Library**
The game uses the `english-words` library (Web2 dictionary), which provides access to over 235,000 English words without requiring an internet connection. This ensures the game works reliably in any environment, including restricted networks or automated grading systems.

**Adaptive Difficulty**
Players choose between three difficulty modes before each game:
- **Easy** — words between 3 and 5 letters, 6 attempts allowed
- **Medium** — words between 6 and 7 letters, 6 attempts allowed
- **Hard** — words of 8 or more letters, 6 attempts allowed

The difficulty affects only the word length, keeping the number of attempts fair across all levels while still making harder words genuinely more challenging to guess.

**ASCII Art Hangman Stages**
The game features 7 progressive ASCII art stages that evolve with every wrong guess, giving the player clear visual feedback on how close they are to losing. This replaces the typical counter-only approach and makes the game feel more engaging in the terminal.

**Input Validation**
The game handles all invalid inputs gracefully — including numbers, symbols, multi-character strings, and repeated guesses — without crashing. The player is always guided with a clear message explaining what went wrong.

---

## Project Structure

**`project.py`**
The core file of the project. Contains the `main()` function and four additional functions:
- `get_word(difficulty)` — Loads the english-words library and returns a random word filtered by the difficulty's length range.
- `get_difficulty()` — Prompts the player to select a difficulty level, accepting both numeric input (1/2/3) and text input (easy/medium/hard). Loops until a valid choice is made.
- `check_guess(letter, word, guessed_letters)` — Validates the guessed letter and checks whether it exists in the target word. Returns True or False.
- `display_board(word, guessed_letters, attempts_left)` — Renders the current hangman ASCII stage, the word progress with blanks and revealed letters, and the list of wrong guesses so far.

**`test_project.py`**
Contains 13 pytest tests covering the three core testable functions: `check_guess`, `get_difficulty`, and `display_board`. Tests cover correct guesses, wrong guesses, case-insensitivity, invalid input, numeric and text difficulty selection, invalid-then-valid input sequences, and board rendering with and without wrong guesses.

**`requirements.txt`**
Lists the two external dependencies: `english-words` for the word library and `pytest` for running the test suite.

---

## Design Choices

**Why english-words instead of an API?**
The original design used the Random Word API (random-word-api.herokuapp.com) to fetch words at runtime. During development, the API proved unreliable — it frequently timed out or returned errors. Switching to the `english-words` library solved this completely: the words are bundled locally, load instantly, and the library supports filtering by alphabet-only words out of the box using `alpha=True`.

**Why keep attempts equal across difficulties?**
An earlier version used different attempt counts per difficulty (8 for easy, 6 for medium, 4 for hard). After testing, this felt punishing on Hard mode — longer words with fewer attempts left almost no room for reasonable play. Keeping 6 attempts for all levels means the difficulty comes from the word complexity, not from an artificially reduced margin for error.

**Why allow both number and text input for difficulty?**
Accepting both `"1"` and `"easy"` as valid inputs makes the game more natural to use. A player who types "hard" directly should not be forced to re-enter "3". The `get_difficulty()` function maps both formats to the same internal value, keeping the logic clean.

---

This was CS50P!
