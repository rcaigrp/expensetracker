import json
import os

DB_FILE = "expenses.json"

def add_expense(amount, category="other"):
    expenses = []
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            try:
                expenses = json.load(f)
            except json.JSONDecodeError:
                expenses = []
    expenses.append({"amount": amount, "category": category})
    with open(DB_FILE, "w") as f:
        json.dump(expenses, f)

def get_expenses():
    expenses = []
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            try:
                expenses = json.load(f)
            except json.JSONDecodeError:
                pass
    return expenses

def get_summary():
    expenses = get_expenses()
    return sum(exp.get("amount", 0) for exp in expenses)
