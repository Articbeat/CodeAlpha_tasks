Hangman Game
A fun, classic word-guessing game where you try to save your hangman friend.

What's This Game About?
Try to guess the secret word one letter at a time. Each wrong guess brings the hangman one step closer to completion.

Quick Start
python hangman.py

That's it - just run and play.

How to Play
The computer picks a random word and shows you blanks representing each letter. You guess one letter at a time. Correct guesses reveal the letter's position. Wrong guesses add a part to the hangman drawing. Guess all letters before the hangman is complete to win.

What You'll See
o
/|\
/ \

Word: a p p _ e
Guessed Letters: a e s

The drawing shows your progress - a full body means game over.

Simple Rules
One letter at a time - keeps the game fair
Letters only - numbers and symbols don't count
Five wrong guesses max - after that, the game ends
No repeat guesses - you can't guess the same letter twice

Current Word List
apple
banana
grape
orange
strawberry

You can easily add more words by editing the WORDS list in the code.

Helpful Reminders
The game will let you know if you type more than one letter, use numbers or symbols, or guess the same letter twice.

Customization Options
Make the game harder by reducing wrong guesses:
MAX_WRONG_GUESSES = 3

Add your own words:
WORDS = ["python", "coding", "hangman", "puzzle"]

Change the hangman drawings:
Modify the DRAWINGS dictionary with your own ASCII art.

Quick Tips
Press Enter after each letter guess
Run the program again for a new game
The game tracks all letters you've guessed

Troubleshooting
If nothing happens when you type, make sure you're pressing Enter after each letter. If you see "invalid input," you probably typed more than one letter - try again with just one.
