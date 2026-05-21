def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x , y = int(x), int(y)
            if x < 0 or y < 0 or x > y:
                continue
            percent = round(x/y * 100)
            break
        except(ValueError, ZeroDivisionError):
            continue
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")
main()
