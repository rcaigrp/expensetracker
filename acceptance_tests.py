import os
import pytest
from expense_tracker import add_expense, get_expenses, get_summary
import expense_tracker

@pytest.fixture
def temp_db():
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        db_path = tmp.name
    expense_tracker.DB_FILE = db_path
    yield db_path
    expense_tracker.DB_FILE = "expenses.json"
    if os.path.exists(db_path):
        os.remove(db_path)

def test_criterion_1_import():
    assert callable(add_expense)
    assert callable(get_expenses)
    assert callable(get_summary)

def test_criterion_2_add_expense(temp_db):
    add_expense(100, "food")
    expenses = get_expenses()
    assert len(expenses) == 1
    assert expenses[0]["amount"] == 100

def test_criterion_3_get_expenses(temp_db):
    add_expense(100, "food")
    add_expense(200, "transport")
    expenses = get_expenses()
    assert len(expenses) == 2

def test_criterion_4_get_summary(temp_db):
    add_expense(100, "food")
    add_expense(200, "transport")
    assert get_summary() == 300
