import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), 'expenses.json')

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f)

def add_expense(amount, category='general', description=''):
    expenses = load_expenses()
    expense = {
        'amount': float(amount),
        'category': category,
        'description': description
    }
    expenses.append(expense)
    save_expenses(expenses)
    return expense

def get_expenses():
    return load_expenses()

def get_summary():
    expenses = load_expenses()
    total = sum(e.get('amount', 0) for e in expenses)
    return {'total': total, 'count': len(expenses)}
