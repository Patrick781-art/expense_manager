
import json

from validator import validate_expense


def save_expense(filename, expenses):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)

        return True

    except (OSError, TypeError, ValueError) as error:
        print("Could not save expenses:", error)
        return False


def load_expenses(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Invalid file format.")
            return []

        valid_expenses = []

        for expense in data:
            if validate_expense(expense):
                valid_expenses.append(expense)

        return valid_expenses

    except (OSError, json.JSONDecodeError) as error:
        print("Could not load expenses:", error)
        return []
