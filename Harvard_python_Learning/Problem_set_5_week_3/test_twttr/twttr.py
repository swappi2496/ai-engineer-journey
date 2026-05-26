def main():
    prompt = input("Input")
    print("Output:", shorten(prompt))

def shorten(word):
    results = ""

    for letter in word:
        if letter.lower() not in "aeiou":
            results += letter
    return results

if __name__ == "__main__":
    main()

