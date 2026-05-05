import random

def play_ground():
    
    secret = random.randint(0, 100)
    guesses = 0
    guess = -1

    while guess != secret:
        guess = int(input("Enter you number: "))
        guesses +=1
        if guess < secret:
            print("Too Low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"Correct! you got it in {guesses} guess")
    return guesses

def main():
    print("welcome to the Guessing Game.")
    while True:
        play_ground()
        reponse = input("Want to play again?(y/n)")
        if reponse.lower() != "y":
            break

main()


