import pytest
import json
import os
import expense_tracker

@pytest.fixture
def clean_db(tmp_path, monkeypatch):
    db_path = str(tmp_path / "expenses.json")
    with open(db_path, 'w') as f:
        f.write("[]")
    monkeypatch.setattr(expense_tracker, 'DB_FILE', db_path)
    yield db_path

def test_criterion_1_import():
    import expense_tracker
    assert hasattr(expense_tracker, 'add_expense')
    assert hasattr(expense_tracker, 'get_expenses')
    assert hasattr(expense_tracker, 'get_summary')

def test_criterion_2_add_expense(clean_db):
    expense_tracker.add_expense(10.0, "food")
    with open(clean_db) as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["amount"] == 10.0

def test_criterion_3_get_expenses(clean_db):
    expense_tracker.add_expense(10.0, "food")
    expenses = expense_tracker.get_expenses()
    assert len(expenses) == 1

def test_criterion_4_get_summary(clean_db):
    expense_tracker.add_expense(10.0, "food")
    expense_tracker.add_expense(20.0, "work")
    summary = expense_tracker.get_summary()
    assert summary["total"] == 30.0
