def main():
    print("=== Tip Caluclator ===")
    bill = get_dollars("Bill amount: ")
    tip_percent = get_percent("Tip percentage: ")
    people = get_int("Number of people: ")

    tip_amount = bill * tip_percent
    subtotal = bill + tip_amount
    per_person = subtotal/ people

    # Print Receipt
    print()
    print(f"Bill amount: ${bill:.2f}")
    print(f"Tip ({tip_percent*100:.0f}%): ${tip_amount:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Splitting between {people} people")
    print(f"Per person: ${per_person:.2f}")
    print("======================")

def get_dollars(prompt):
    while True:
        try:
            value = input(prompt).strip().lstrip("$")
            return float(value)
        except ValueError:
            print("Invalid amount, try again.")

def get_percent(prompt):
    while True:
        try:
            value = input(prompt).strip().rstrip("%")
            value = float(value)
            if 0 <= value <=100:
                return value/100
            print("Percentage mush be between 0 and 100.")
        except ValueError:
            print("invalid percentage, try again.")

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print("Must be a positive number")
        except ValueError:
            print("Invalid number, try again.")

main()
