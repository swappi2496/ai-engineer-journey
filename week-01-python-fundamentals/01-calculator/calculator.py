#calculator.py - a simple command-line calculator
#Built on Day 1 of my AI engineer journey

def calculate(a, op, b):
    #Tkae two numbers and an operator, return the results
    if op == '+':
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b
    elif op == "/":
        if b == 0:
            return "Error: cannot divide by zero"
    else:
        return f"unknown operator: {op}"

def main():
    print("Simple Calculator")
    print("-----------------")

    #input() always returns a string: convert to float for math
    a = float(input("First number: "))
    op = input("Select Operator (+, -, *, /): ")
    b = float(input("Second Number: "))

    result = calculate(a, op, b)
    print(f"Result: {result}")

#This lines runs main() when the file is executed
if __name__ == '__main__':
    main()