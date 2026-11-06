
import math


def validate_expense(expense):
    # Expense must be a dictionary
    if not isinstance(expense, dict):
        return False

    # Amount must exist
    if "amount" not in expense:
        return False

    # Boolean values are not valid amounts
    if isinstance(expense["amount"], bool):
        return False

    # Convert amount into a number
    try:
        amount = float(expense["amount"])
    except (ValueError, TypeError):
        return False

    # Reject infinity, NaN and negative amounts
    if not math.isfinite(amount) or amount < 0:
        return False

    return True
