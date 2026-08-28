import json
from datetime import datetime

FILE = "expenses.json"


def load_expenses():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    description = input("What did you spend money on? ")
    amount = float(input("Amount: ₦"))
    category = input("Category (Food/Transport/School/Other): ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("✅ Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- YOUR EXPENSES ---")

    for expense in expenses:
        print(
            f"{expense['date']} | "
            f"{expense['description']} | "
            f"{expense['category']} | "
            f"₦{expense['amount']:.2f}"
        )


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\n💰 Total spending: ₦{total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== STUDENT EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()
