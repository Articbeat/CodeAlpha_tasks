import random

WORDS = ["apple", "banana", "grape", "orange", "strawberry"]
MAX_WRONG_GUESSES = 5

DRAWINGS = {
    0: ("   ", "   ", "   "),
    1: (" o  ", " |  ", "   "),
    2: (" o  ", "/|  ", "   "),
    3: (" o  ", "/|\\ ", "   "),
    4: (" o  ", "/|\\ ", "/  "),
    5: (" o  ", "/|\\ ", "/ \\"),
}

def display_drawing(wrong_guesses):
    print("\n********")
    for line in DRAWINGS[wrong_guesses]:
        print(line)
    print("********")

def display_hint(hint):
    print("Word:", " ".join(hint))

def display_guessed_letters(guessed_letters):
    print("Guessed Letters:", " ".join(sorted(guessed_letters)))

def main():
    answer = random.choice(WORDS)
    hint = ["_"] * len(answer)
    guessed_letters = set()
    wrong_guesses = 0

    while True:
        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print("Wrong guess")

        display_drawing(wrong_guesses)
        display_hint(hint)
        display_guessed_letters(guessed_letters)

        if wrong_guesses == MAX_WRONG_GUESSES:
            print(f"You lose! The word was {answer}")
            break

        if "_" not in hint:
            print("You win!")
            break

if __name__ == "__main__":
    main()
