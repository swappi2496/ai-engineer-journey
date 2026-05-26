def main():
    gretting = input("Gretting: ")
    print(f"${value(gretting)}")

def value(gretting):
    g = gretting.strip().lower()
    if g.startswith("hello"):
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
