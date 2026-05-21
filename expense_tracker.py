import json
import os

DB_FILE = "expenses.json"

def _load():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def _save(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f)

def add_expense(amount, category):
    data = _load()
    data.append({"amount": amount, "category": category})
    _save(data)

def get_expenses():
    return _load()

def get_summary():
    data = _load()
    total = sum(e["amount"] for e in data)
    return {"total": total}
