import pytest
import os
import tempfile
import sys

sys.path.insert(0, os.path.dirname(__file__))
import expense_tracker

DATA_FILE = os.path.join(tempfile.gettempdir(), "test_expenses.json")

@pytest.fixture
def setup_teardown():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    expense_tracker.DATA_FILE = DATA_FILE
    yield
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_criterion_1_import():
    try:
        import expense_tracker
    except ImportError:
        pytest.fail("Module not importable")

def test_criterion_2_add_expense(setup_teardown):
    expense_tracker.add_expense(100, "food", "lunch")
    data = expense_tracker._load_data()
    assert len(data) == 1
    assert data[0]['amount'] == 100

def test_criterion_3_get_expenses(setup_teardown):
    expense_tracker.add_expense(100, "food", "lunch")
    expenses = expense_tracker.get_expenses()
    assert len(expenses) == 1

def test_criterion_4_get_summary(setup_teardown):
    expense_tracker.add_expense(100, "food", "lunch")
    expense_tracker.add_expense(200, "work", "overtime")
    summary = expense_tracker.get_summary()
    assert summary['total'] == 300
    assert summary['count'] == 2
