import random

def main():
    n = get_positive_int("Level: ")
    secret = random.randint(1, n)

    while True:
            guess = get_positive_int("Guess: ")

            if guess < secret:
                print("Too small!")
            elif guess > secret:
                print("Too large!")
            else:
                print("Just right!")
                break

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
main()

