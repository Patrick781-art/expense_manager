
import json

from validator import validate_expense
from storage import save_expense, load_expenses


def test_missing_key():
    assert not validate_expense({"category": "Travel"})


def test_invalid_string():
    assert not validate_expense({"amount": "abc"})


def test_negative_number():
    assert not validate_expense({"amount": -100})


def test_zero():
    assert validate_expense({"amount": 0})


def test_boolean():
    assert not validate_expense({"amount": True})


def test_valid_expense():
    assert validate_expense({
        "category": "Food",
        "amount": 100
    })


def test_not_dictionary():
    assert not validate_expense("invalid")


def test_save_and_load(tmp_path):
    filename = tmp_path / "expenses.json"

    expenses = [
        {"category": "Food", "amount": 100},
        {"category": "Travel", "amount": 200}
    ]

    assert save_expense(filename, expenses) is True
    assert load_expenses(filename) == expenses


def test_missing_file(tmp_path):
    filename = tmp_path / "missing.json"

    assert load_expenses(filename) == []


def test_corrupt_json(tmp_path):
    filename = tmp_path / "corrupt.json"
    filename.write_text("{invalid json", encoding="utf-8")

    assert load_expenses(filename) == []


def test_invalid_records_are_filtered(tmp_path):
    filename = tmp_path / "expenses.json"

    data = [
        {"category": "Food", "amount": 100},
        {"category": "Travel", "amount": "bad"},
        {"category": "Shopping", "amount": -50}
    ]

    filename.write_text(json.dumps(data), encoding="utf-8")

    assert load_expenses(filename) == [
        {"category": "Food", "amount": 100}
    ]
