import os
import tempfile
import pytest
import expense_tracker

@pytest.fixture
def setup_db():
    expense_tracker.DB_FILE = tempfile.mktemp(suffix=".json")
    yield
    os.remove(expense_tracker.DB_FILE)

def test_criterion_1_import():
    assert hasattr(expense_tracker, 'add_expense')
    assert hasattr(expense_tracker, 'get_expenses')
    assert hasattr(expense_tracker, 'get_summary')

def test_criterion_2_add_expense(setup_db):
    expense_tracker.add_expense({"amount": 10, "category": "food"})
    expenses = expense_tracker.get_expenses()
    assert len(expenses) == 1
    assert expenses[0]["amount"] == 10

def test_criterion_3_get_expenses(setup_db):
    expense_tracker.add_expense({"amount": 5, "category": "transport"})
    expense_tracker.add_expense({"amount": 15, "category": "food"})
    expenses = expense_tracker.get_expenses()
    assert len(expenses) == 2
    assert expenses[0]["category"] == "transport"
    assert expenses[1]["category"] == "food"

def test_criterion_4_get_summary(setup_db):
    expense_tracker.add_expense({"amount": 10, "category": "food"})
    expense_tracker.add_expense({"amount": 20, "category": "transport"})
    expense_tracker.add_expense({"amount": 5, "category": "misc"})
    assert expense_tracker.get_summary() == 35
