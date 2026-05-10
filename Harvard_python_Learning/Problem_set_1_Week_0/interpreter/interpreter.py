parts = input("Enter you want to '+, -, *, /' in the form of 1 + 1: ")
x, y, z = parts.split()
x = int(x)
z = int(z)
if y == "+":
    result = x + z
elif y == "-":
    result = x-z
elif y == "*":
    result = x*z
elif y == "/":
    result = x/z
else:
    print("Invalid Input")

print(f"{result:.1f}")
