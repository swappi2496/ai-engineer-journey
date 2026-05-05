# Number Guessing Game

A command-line guessing game where the computer picks a random number between 1 and 100, and the player keeps guessing until they get it right. Tracks the number of guesses and lets the player replay as many rounds as they want.

## What I learned:
- Important external modules with `import random` and uaing `random.randint(1, 100)` 
- The `while True:` + `break` pattern as a clean way to loop until a condition is met
- Counter variables (`guesses +=1`)
- f-string for formatted output(`f"Correct! you got it in {guesses} guess"`)
- String method `.lower()` to make input case-insensitive (so "Y" and "y" both work)
- Splitting logic into multiple functions: one for a single round, one for the overall game flow
- Returning values from functions with `return`

## How it run:
```bash
python number_guess.py
```

## Sample run
```
Welcome to the Guessing Game.
Enter your number: 50
Too high
Enter your number: 25
Too Low
Enter your number: 37
Too high
Enter your number: 31
Correct! you got it in 4 guess
Want to play again? (y/n): n
Thanks for playing!
```

