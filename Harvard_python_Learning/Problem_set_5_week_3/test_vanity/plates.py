def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False

    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    if not plate.isalnum():
        return False

    found_number = False

    for char in plate:
        if char.isdigit():
            if not found_number:
                if char == "0":
                    return False
                found_number = True
        else:
            if found_number:
                return False

    return True

if __name__ == "__main__":
    main()
