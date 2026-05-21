import json
import os

DB_FILE = "expenses.json"

def add_expense(amount, category, description="", db_file=None):
    file = db_file or DB_FILE
    expenses = []
    if os.path.exists(file):
        with open(file, "r") as f:
            try:
                expenses = json.load(f)
            except json.JSONDecodeError:
                expenses = []
    expenses.append({"amount": amount, "category": category, "description": description})
    with open(file, "w") as f:
        json.dump(expenses, f)
    return True

def get_expenses(db_file=None):
    file = db_file or DB_FILE
    expenses = []
    if os.path.exists(file):
        with open(file, "r") as f:
            try:
                expenses = json.load(f)
            except json.JSONDecodeError:
                expenses = []
    return expenses

def get_summary(db_file=None):
    expenses = get_expenses(db_file)
    total = sum(e.get("amount", 0) for e in expenses)
    return total
