
from validator import validate_expense
from storage import save_expense, load_expenses


FILENAME = "expenses.json"


def add_expense(expenses):
    category = input("Enter expense category: ").strip()
    amount = input("Enter expense amount: ").strip()

    expense = {
        "category": category,
        "amount": amount
    }

    if not category:
        print("Category cannot be empty.")
        return

    if not validate_expense(expense):
        print("Invalid amount. Please enter a valid non-negative number.")
        return

    expense["amount"] = float(amount)
    expenses.append(expense)

    if save_expense(FILENAME, expenses):
        print("Expense added successfully!")
    else:
        expenses.pop()
        print("Expense was not saved.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Your Expenses ---")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} - "
            f"{expense['amount']}"
        )


def show_total(expenses):
    total = sum(float(expense["amount"]) for expense in expenses)

    print(f"\nTotal spending: {total:.2f}")


def main():
    expenses = load_expenses(FILENAME)

    while True:
        print("\n===== EXPENSE MANAGER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total spending")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()


