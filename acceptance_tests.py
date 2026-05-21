import os
import pytest
import sys

# Add the project directory to sys.path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

import expense_tracker

DATA_FILE = expense_tracker.DATA_FILE

@pytest.fixture
def clean_data():
    """Ensure the data file is clean before and after each test."""
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    yield
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_criterion_1_module_import():
    """Test that the expense_tracker module can be imported and has required functions."""
    assert hasattr(expense_tracker, 'add_expense')
    assert hasattr(expense_tracker, 'get_expenses')
    assert hasattr(expense_tracker, 'get_summary')

def test_criterion_2_add_expense(clean_data):
    """Test that add_expense saves an expense."""
    expense = {"id": 1, "amount": 50.0, "category": "Food"}
    result = expense_tracker.add_expense(expense)
    assert result is True
    saved_expenses = expense_tracker.get_expenses()
    assert len(saved_expenses) == 1
    assert saved_expenses[0] == expense

def test_criterion_3_get_expenses(clean_data):
    """Test that get_expenses retrieves all expenses."""
    expense1 = {"id": 1, "amount": 10.0, "category": "Book"}
    expense2 = {"id": 2, "amount": 20.0, "category": "Food"}
    expense_tracker.add_expense(expense1)
    expense_tracker.add_expense(expense2)
    expenses = expense_tracker.get_expenses()
    assert len(expenses) == 2

def test_criterion_4_get_summary(clean_data):
    """Test that get_summary returns total spent."""
    expense1 = {"id": 1, "amount": 10.0, "category": "Book"}
    expense2 = {"id": 2, "amount": 20.0, "category": "Food"}
    expense_tracker.add_expense(expense1)
    expense_tracker.add_expense(expense2)
    summary = expense_tracker.get_summary()
    assert summary == 30.0
