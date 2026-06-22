import json
import os

def load_transactions(filename = "transactions.json"):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename) as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    
def save_transactions(transaction, filename = 'transaction.json'):
    with open(filename, 'w') as f:
        json.dump(transaction, f, indent = 2)
