class Expense:
    def __init__(self, expense_id, title, amount, category, date):
        self.expense_id = expense_id
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return (
            f"ID: {self.expense_id} | "
            f"Title: {self.title} | "
            f"Amount: ₹{self.amount:.2f} | "
            f"Category: {self.category} | "
            f"Date: {self.date}"
        )