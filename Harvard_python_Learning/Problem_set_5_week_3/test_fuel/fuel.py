def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
    except(ValueError, ZeroDivisionError):
        print("Invalid Input")
        return
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0:
        raise ValueError
    if x > y:
        raise ValueError
    return round(x / y * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
