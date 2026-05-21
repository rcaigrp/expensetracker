import pytest
import os
import json
import expense_tracker

@pytest.fixture
def mock_expense_file(tmp_path, monkeypatch):
    test_file = tmp_path / "test_expenses.json"
    monkeypatch.setattr(expense_tracker, 'DATA_FILE', str(test_file))
    yield test_file

def test_criterion_1_module_exists():
    import expense_tracker
    assert expense_tracker is not None

def test_criterion_2_add_expense_saves(mock_expense_file):
    expense_tracker.add_expense(10.50, category='food', description='Lunch')
    with open(mock_expense_file, 'r') as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]['amount'] == 10.50
    assert data[0]['category'] == 'food'

def test_criterion_3_get_expenses_retrieves(mock_expense_file):
    expense_tracker.add_expense(10.50, category='food', description='Lunch')
    expense_tracker.add_expense(20.00, category='transport', description='Uber')
    expenses = expense_tracker.get_expenses()
    assert len(expenses) == 2
    assert expenses[0]['amount'] == 10.50

def test_criterion_4_get_summary_returns_total(mock_expense_file):
    expense_tracker.add_expense(10.50, category='food', description='Lunch')
    expense_tracker.add_expense(20.00, category='transport', description='Uber')
    summary = expense_tracker.get_summary()
    assert summary['total'] == 30.50
    assert summary['count'] == 2
