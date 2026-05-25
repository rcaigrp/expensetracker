import os
import json
import pytest
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import expense_tracker

@pytest.fixture
def clean_expenses_file():
    data_file = expense_tracker.DATA_FILE
    if os.path.exists(data_file):
        os.remove(data_file)
    yield
    if os.path.exists(data_file):
        os.remove(data_file)

def test_criterion_1_module_exists():
    assert hasattr(expense_tracker, 'add_expense')
    assert hasattr(expense_tracker, 'get_expenses')

def test_criterion_2_add_expense(clean_expenses_file):
    expense_tracker.add_expense(100, "Food", "Lunch")
    assert os.path.exists(expense_tracker.DATA_FILE)
    with open(expense_tracker.DATA_FILE, "r") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["amount"] == 100

def test_criterion_3_get_expenses(clean_expenses_file):
    expense_tracker.add_expense(50, "Transport", "Bus")
    expenses = expense_tracker.get_expenses()
    assert isinstance(expenses, list)
    assert len(expenses) == 1
    assert expenses[0]["category"] == "Transport"
