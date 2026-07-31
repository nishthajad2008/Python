class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def get_balance(self):
        # Calculate current balance from ledger entries
        return sum(item["amount"] for item in self.ledger)

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        # Returns False if amount exceeds balance, True otherwise
        if amount > self.get_balance():
            return False
        return True

    def withdraw(self, amount, description=""):
        # Uses check_funds to validate the withdrawal
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, budget_category):
        # Uses check_funds to validate the entire transfer execution
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.name}")
            budget_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        # 1. Title line: 30 chars total, category name centered between *
        title = f"{self.name:*^30}\n"

        # 2. Ledger lines: 23 chars left-aligned description, 7 chars right-aligned amount
        ledger_lines = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            ledger_lines += f"{desc:<23}{amount:>7}\n"

        # 3. Total line
        total_line = f"Total: {self.get_balance():.2f}"

        return title + ledger_lines + total_line


def create_spend_chart(categories):
    # 1. Calculate the total withdrawals per category and overall total
    total_spent = 0
    category_spent = []

    for category in categories:
        spent = 0
        for item in category.ledger:
            # Withdrawals have a negative amount
            if item["amount"] < 0:
                spent += abs(item["amount"])
        category_spent.append(spent)
        total_spent += spent

    # 2. Calculate percentages rounded down to the nearest 10
    # Handle division by zero edge case if total_spent is 0
    percentages = []
    for spent in category_spent:
        if total_spent > 0:
            percentage = (spent / total_spent) * 100
            # Round down to the nearest 10 (e.g., 66.6 -> 60)
            percentages.append(int(percentage // 10) * 10)
        else:
            percentages.append(0)

    # 3. Build the chart title
    chart = "Percentage spent by category\n"

    # 4. Generate the y-axis and bar graph lines
    for i in range(100, -1, -10):
        # Format the y-axis numbers to align right with width 3
        chart += f"{i:3d}|"
        for pct in percentages:
            if pct >= i:
                chart += " o "
            else:
                chart += "   "
        # Pad one extra space at the end of the line
        chart += " \n"

    # 5. Generate the horizontal separator line
    # 4 spaces for the y-axis padding ("100|") + 3 spaces per category
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 6. Generate the vertical category labels
    max_len = max(len(category.name) for category in categories)
    # Pad shorter names with spaces to match the longest name length
    names = [category.name.ljust(max_len) for category in categories]

    for i in range(max_len):
        chart += "    "
        for name in names:
            chart += f" {name[i]} "
        # Pad one extra space at the end of the line, skip final newline
        chart += " "
        if i < max_len - 1:
            chart += "\n"

    return chart
