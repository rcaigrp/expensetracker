import json
import os

DB_FILE = "expenses.json"

def load():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def add_expense(expense):
    data = load()
    data.append(expense)
    save(data)

def get_expenses():
    return load()

def get_summary():
    return sum(exp.get("amount", 0) for exp in get_expenses())
