import csv
from expense import Expense


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("\nExpense added successfully!\n")

    def view_expenses(self):

        if not self.expenses:
            print("\nNo expenses found.\n")
            return

        print("\n" + "=" * 90)

        print(
            f"{'ID':<8}"
            f"{'TITLE':<25}"
            f"{'AMOUNT':<15}"
            f"{'CATEGORY':<20}"
            f"{'DATE':<15}"
       )

        print("=" * 90)

        for expense in self.expenses:

            print(
                f"{expense.expense_id:<8}"
                f"{expense.title:<25}"
                f"₹{expense.amount:<14.2f}"
                f"{expense.category:<20}"
                f"{expense.date:<15}"
            )

        print("=" * 90)

    def search_expense(self, expense_id):
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                return expense

        return None

    def update_expense(self, expense_id, title=None, amount=None, category=None, date=None):
        expense = self.search_expense(expense_id)

        if expense is None:
            print("\nExpense not found.\n")
            return

        if title is not None:
            expense.title = title

        if amount is not None:
            expense.amount = amount

        if category is not None:
            expense.category = category

        if date is not None:
            expense.date = date

        print("\nExpense updated successfully!\n")

    def delete_expense(self, expense_id):
        expense = self.search_expense(expense_id)

        if expense is None:
            print("\nExpense not found.\n")
            return

        self.expenses.remove(expense)

        print("\nExpense deleted successfully!\n")

    def save_to_csv(self):
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "expense_id",
                "title",
                "amount",
                "category",
                "date"
            ])

            for expense in self.expenses:
                writer.writerow([
                    expense.expense_id,
                    expense.title,
                    expense.amount,
                    expense.category,
                    expense.date
              ])

    print("\nExpenses saved successfully!\n")

    def load_from_csv(self):
        try:
            with open("expenses.csv", "r", newline="") as file:
                reader = csv.DictReader(file)

                self.expenses = []

                for row in reader:
                    expense = Expense(
                        int(row["expense_id"]),
                        row["title"],
                        float(row["amount"]),
                        row["category"],
                        row["date"]
                    )

                    self.expenses.append(expense)

            print("\nExpenses loaded successfully!\n")

        except FileNotFoundError:
            print("\nNo previous expense data found.\n")

    def view_summary(self):

        if not self.expenses:
            print("\nNo expenses found.\n")
            return

        total = 0
        category_summary = {}

        for expense in self.expenses:

           total += expense.amount

           if expense.category in category_summary:
               category_summary[expense.category] += expense.amount
           else:
               category_summary[expense.category] = expense.amount

        print("\n" + "=" * 55)
        print("              EXPENSE SUMMARY")
        print("=" * 55)

        print(f"Total Records : {len(self.expenses)}")
        print(f"Total Expense : ₹{total:.2f}")

        print("\nCategory-wise Spending:")

        for category, amount in category_summary.items():
            print(f"{category:<20} ₹{amount:.2f}")

        print("=" * 55)

    def generate_expense_id(self):
        if not self.expenses:
            return 101

        return max(expense.expense_id for expense in self.expenses) + 1