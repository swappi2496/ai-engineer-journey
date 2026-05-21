prompt = input("Input: ")

result = ""

for letter in prompt:
    if letter.lower() not in "aeiou":
        result +=letter
print(f"Output: {result}")
