answer = input("what is the answer to the great question of life, the universe, and everything?").strip().lower()

if answer in ["42", "forty two", "forty-two"]:
    print("Yes")
else:
    print("No")
