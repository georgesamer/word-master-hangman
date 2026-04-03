import random
import sys
from english_words import get_english_words_set


HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

DIFFICULTY_SETTINGS = {
    "easy":   {"min_len": 3, "max_len": 5, "attempts": 6},
    "medium": {"min_len": 6, "max_len": 7, "attempts": 6},
    "hard":   {"min_len": 8, "max_len": 20, "attempts": 6},
}



def main():
    print("=" * 45)
    print("       Welcome to Hangman!")
    print("=" * 45)

    difficulty = get_difficulty()
    word = get_word(difficulty)

    if not word:
        print("Could not fetch a word. Please check your internet connection.")
        sys.exit(1)

    word = word.lower()
    guessed_letters = set()
    settings = DIFFICULTY_SETTINGS[difficulty]
    attempts_left = settings["attempts"]

    print(f"\nDifficulty: {difficulty.capitalize()}")
    print(f"The word has {len(word)} letters. You have {attempts_left} attempts.\n")

    while attempts_left > 0:
        display_board(word, guessed_letters, attempts_left)

        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        correct = check_guess(guess, word, guessed_letters)
        guessed_letters.add(guess)

        if correct:
            print(f"✓ '{guess}' is in the word!")
        else:
            attempts_left -= 1
            print(f"✗ '{guess}' is not in the word. {attempts_left} attempts left.")

        if all(letter in guessed_letters for letter in word):
            display_board(word, guessed_letters, attempts_left)
            print(f"\n🎉 You won! The word was: {word.upper()}")
            return

    print(HANGMAN_STAGES[-1])
    print(f"\n💀 Game over! The word was: {word.upper()}")


def get_difficulty():
    """Ask the user to choose a difficulty level and return it as a string."""
    print("\nChoose difficulty:")
    print("  1. Easy   (3–5 letters, 8 attempts)")
    print("  2. Medium (6–7 letters, 6 attempts)")
    print("  3. Hard   (8+ letters,  4 attempts)")

    choices = {"1": "easy", "2": "medium", "3": "hard",
               "easy": "easy", "medium": "medium", "hard": "hard"}

    while True:
        choice = input("Enter 1, 2, 3 (or easy/medium/hard): ").strip().lower()
        if choice in choices:
            return choices[choice]
        print("Invalid choice. Please enter 1, 2, 3, easy, medium, or hard.")


def get_word(difficulty):
    """Return a random word from the english-words library matching the difficulty length range."""
    settings = DIFFICULTY_SETTINGS.get(difficulty)
    if not settings:
        return None

    min_len = settings["min_len"]
    max_len = settings["max_len"]

    words = get_english_words_set(["web2"], lower=True, alpha=True)
    filtered = [w for w in words if min_len <= len(w) <= max_len]

    if filtered:
        return random.choice(filtered)

    return None


def check_guess(letter, word, guessed_letters):
    """Return True if the letter is in the word and not already guessed, else False."""
    if len(letter) != 1 or not letter.isalpha():
        return False
    return letter.lower() in word.lower()


def display_board(word, guessed_letters, attempts_left):
    """Print the hangman figure, the word progress, and guessed letters."""
    max_attempts = 6
    stage_index = max_attempts - min(attempts_left, max_attempts)
    stage_index = max(0, min(stage_index, len(HANGMAN_STAGES) - 1))

    print(HANGMAN_STAGES[stage_index])

    word_display = " ".join(
        letter if letter in guessed_letters else "_" for letter in word
    )
    print(f"\n  Word: {word_display}")

    if guessed_letters:
        wrong = sorted(l for l in guessed_letters if l not in word)
        if wrong:
            print(f"  Wrong guesses: {', '.join(wrong)}")


if __name__ == "__main__":
    main()