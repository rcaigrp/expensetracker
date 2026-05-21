import json
import os

DATA_FILE = "expense_tracker_data.json"

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

def add_expense(expense):
    """Add an expense to the data file."""
    data = _load_data()
    data.append(expense)
    _save_data(data)
    return True

def get_expenses():
    """Retrieve all expenses."""
    return _load_data()

def get_summary():
    """Return the total amount spent."""
    data = _load_data()
    return sum(expense.get('amount', 0) for expense in data)
