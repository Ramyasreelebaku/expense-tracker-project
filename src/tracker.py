from datetime import date
from tabulate import tabulate
from collections import defaultdict
 
 
def _validate_amount(amount_str: str) -> float | None:
    """Validate and convert amount string to float."""
    if not amount_str.strip():
        print("Amount cannot be empty.")
        return None
    
    try:
        amount = float(amount_str)
        if amount <= 0:
            print("Amount must be greater than 0.")
            return None
        return amount
    except ValueError:
        print("Amount must be a number.")
        return None
 
 
def add_expense(expenses: list[dict]) -> None:
    """Ask user details and add a new expense dictionary into the list."""
    amount = _validate_amount(input("Amount: "))
    if amount is None:
        return
    
    category = input("Category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return
    
    description = input("Description: ").strip()
 
    expenses.append({
        "date": str(date.today()),
        "amount": amount,
        "category": category,
        "description": description
    })
 
 
def list_expenses(expenses: list[dict]) -> None:
    """Print all expenses in a table format."""
    print("\nAll expenses")
 
    if not expenses:
        print("No expenses found yet.")
        return
 
    rows = [[e["date"], e["amount"], e["category"], e["description"]] for e in expenses]
    print(tabulate(rows, headers=["Date", "Amount", "Category", "Description"], tablefmt="grid"))
 
 
def show_total(expenses: list[dict]) -> None:
    """Print total spending."""
    total = sum(float(e["amount"]) for e in expenses) if expenses else 0.0
    print(f"\nTotal spending: ₹{total:.2f}")
 
 
def show_category_summary(expenses: list[dict]) -> None:
    """Print spending summary by category."""
    print("\nCategory summary")
 
    if not expenses:
        print("No expenses found yet.")
        return
 
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense["category"]] += float(expense["amount"])
 
    rows = [[cat, f"₹{amt:.2f}"] for cat, amt in sorted(summary.items())]
    print(tabulate(rows, headers=["Category", "Total"], tablefmt="grid"))