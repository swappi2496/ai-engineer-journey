def main():
    emotions = input("Give your emotions here(for ex: ':), or :( )') and it will convert it to emoji: ")
    print(faces(emotions))

def faces(emotions):
    return emotions.replace(":)", "🙂").replace(":(", "🙁")

main()
