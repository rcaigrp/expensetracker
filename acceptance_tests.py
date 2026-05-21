import pytest
import json
import os
from expense_tracker import add_expense, get_expenses, get_summary

def test_criterion_1_import():
    import expense_tracker
    assert expense_tracker is not None

def test_criterion_2_add_expense(tmpdir):
    db_file = str(tmpdir / "test_expenses.json")
    result = add_expense(10.0, "food", "lunch", db_file=db_file)
    assert result == True
    assert os.path.exists(db_file)
    with open(db_file, "r") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["amount"] == 10.0

def test_criterion_3_get_expenses(tmpdir):
    db_file = str(tmpdir / "test_expenses.json")
    add_expense(5.0, "transport", "bus", db_file=db_file)
    expenses = get_expenses(db_file=db_file)
    assert len(expenses) == 1
    assert expenses[0]["amount"] == 5.0

def test_criterion_4_get_summary(tmpdir):
    db_file = str(tmpdir / "test_expenses.json")
    add_expense(10.0, "food", db_file=db_file)
    add_expense(5.0, "transport", db_file=db_file)
    summary = get_summary(db_file=db_file)
    assert summary == 15.0
