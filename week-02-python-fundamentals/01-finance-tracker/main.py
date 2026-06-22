from transactions import add_transactions, view_balance, list_transactions, filter_by_category, monthly_summary
from storage import load_transactions, save_transactions
from datetime import date as date_module

def main():
    transactions = load_transactions()
    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Transactions\n2. View Balance\n3. List Transactions\n4. Filter by Category\n5. Monthly Summary\n6. Quit")
        choice = input("Choose: ").strip()
        
        if choice == "1":

            type_ = input("Type (income/expense): ").strip().lower()
            if type_ not in ("income", "expense"):
                print("Invalid Type"); continue
            try:
                amount = float(input("Amount: "))

            except ValueError:
                print("Invalid amount"); continue
            
            category = input("Category: ").strip()
            d = input("Date (YYYY-MM-DD, blank for today): ").strip()
            date_str = d if d else date_module.today().isoformat()
            add_transactions(transactions, type_, amount, category, date_str)
            save_transactions(transactions)
            print(f"Added {type_} of ${amount:.2f} in {category} on {date_str}.")

        elif choice == "2":

            bal, inc, exp = view_balance(transactions)
            print(f"Balance: ${bal:.2f} (income ${inc:.2f}, expense ${exp:.2f})")

        elif choice == "3":

            list_transactions(transactions)

        elif choice == "4":

            cat = input("Category: ").strip()
            list_transactions(filter_by_category(transactions, cat))

        elif choice == "5":
            ym = input("Year-Month (YYYY-MM): ").strip()
            inc, exp, net, big = monthly_summary(transactions, ym)
            print(f"Income £{inc:.2f} | Expense £{exp:.2f} | Net £{net:.2f}")
            if big:
                print(f"Biggest expense: £{big['amount']:.2f} in {big['category']} on {big['date']}")
            else:
                print("No expenses recorded for this month.")

        elif choice == "6":

            break

        else:

            print("Invalid Choice")

if __name__ == "__main__":
    main()
