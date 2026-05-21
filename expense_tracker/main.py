import json
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'expenses.json')

def _load_expenses():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def _save_expenses(expenses):
    with open(DB_PATH, 'w') as f:
        json.dump(expenses, f)

def add_expense(amount, category):
    expenses = _load_expenses()
    expenses.append({'amount': amount, 'category': category})
    _save_expenses(expenses)

def get_expenses():
    return _load_expenses()

def get_summary():
    expenses = _load_expenses()
    return sum(e['amount'] for e in expenses)
