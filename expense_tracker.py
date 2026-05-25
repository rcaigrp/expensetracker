import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.json")

def _load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def _save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(amount, category, description):
    expenses = _load_expenses()
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })
    _save_expenses(expenses)

def get_expenses():
    return _load_expenses()
