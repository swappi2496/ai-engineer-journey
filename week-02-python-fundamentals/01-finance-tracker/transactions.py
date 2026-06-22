def add_transactions(transactions, type_, amount, category, date):
    transactions.append({
        "type": type_,
        "amount": amount,
        "category": category,
        "date": date
    })

def view_balance(transactions):
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense") 
    return income - expense, income, expense

def list_transactions(transactions):
    for t in transactions:
        print(f"{t['date']} | {t['type']:7} | ${t['amount']:7.2f} | {t['category']}")

def filter_by_categpry(transactions, category):
    return [t for t in transactions if t["category"].lower() == category.lower()]

def monthly_summary(transactions, year_month):
    rel = [t for t in transactions if t['date'].startswith(year_month)]
    income = sum(t["amount"] for t in rel if t["type"] == "income")
    expense = sum(t["amount"] for t in rel if t["type"] == "expense")
    biggest = max((t for t in rel if t["type"] == "expense"), key = lambda t: t["amount"], default = None)
