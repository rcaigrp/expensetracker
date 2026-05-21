import json
import os

DATA_FILE = "expenses.json"

def _load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def _save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def add_expense(amount, category, description=""):
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    data = _load_data()
    data.append(expense)
    _save_data(data)

def get_expenses():
    return _load_data()

def get_summary():
    expenses = get_expenses()
    total = sum(exp['amount'] for exp in expenses)
    return {"total": total, "count": len(expenses)}
