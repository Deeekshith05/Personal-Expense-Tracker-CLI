from tracker import ExpenseTracker
from expense import Expense
from datetime import datetime

tracker = ExpenseTracker()
tracker.load_from_csv()

while True:

    print("\n" + "=" * 45)
    print("      PERSONAL EXPENSE TRACKER")
    print("=" * 45)

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. View Summary")
    print("7. Save and Exit")

    choice = input("\nEnter your choice (1-7): ").strip()

    if choice == "1":

        expense_id = tracker.generate_expense_id()

        
        while True:
            title = input("Enter Expense Title: ").strip().title()

            if title == "":
                print("Title cannot be empty.\n")
            else:
                break

        
        while True:

            try:
                amount = float(input("Enter Expense Amount: "))

                if amount <= 0:
                    print("Amount must be greater than zero.\n")
                    continue

                break

            except ValueError:
                print("Invalid amount. Please enter a valid number.\n")

        
        while True:

            category = input("Enter Expense Category: ").strip().title()

            if category == "":
                print("Category cannot be empty.\n")
            else:
                break

        
        while True:

            date = input(
                "Enter Date (DD-MM-YYYY) or press Enter for today: "
            ).strip()

            if date == "":
                date = datetime.now().strftime("%d-%m-%Y")
                break

            try:
                datetime.strptime(date, "%d-%m-%Y")
                break

            except ValueError:
                print("Invalid date format. Please use DD-MM-YYYY.\n")

        expense = Expense(
            expense_id,
            title,
            amount,
            category,
            date
        )

        tracker.add_expense(expense)

    elif choice == "2":

        tracker.view_expenses()

    elif choice == "3":

        try:
            expense_id = int(input("Enter Expense ID to search: "))

            expense = tracker.search_expense(expense_id)

            if expense:
                print("\nExpense Found:\n")
                print(expense)
            else:
                print("\nExpense not found.")

        except ValueError:
            print("\nInvalid ID. Please enter a number.")

    elif choice == "4":

        try:
            expense_id = int(input("Enter Expense ID to update: "))

            expense = tracker.search_expense(expense_id)

            if expense is None:
                print("\nExpense not found.")
                continue

            print("\nLeave a field blank if you don't want to change it.\n")

            title = input(f"Title ({expense.title}): ").strip()

            amount_input = input(f"Amount ({expense.amount}): ").strip()

            category = input(f"Category ({expense.category}): ").strip()

            date = input(f"Date ({expense.date}): ").strip()

            if title == "":
                title = None

            if category == "":
                category = None

            if date == "":
                date = None

            if amount_input == "":
                amount = None
            else:
                amount = float(amount_input)

            tracker.update_expense(
                expense_id,
                title,
                amount,
                category,
                date
          )

        except ValueError:
            print("\nInvalid input.")

    elif choice == "5":

        try:
            expense_id = int(input("Enter Expense ID to delete: "))

            tracker.delete_expense(expense_id)

        except ValueError:
            print("\nInvalid Expense ID.")

    elif choice == "6":

        tracker.view_summary()

    elif choice == "7":

        tracker.save_to_csv()

        print("\nThank you for using Personal Expense Tracker.")

        break

    else:

        print("\nInvalid choice. Please enter a number between 1 and 7.")