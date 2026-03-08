from storage import load_expenses, save_expenses
from tracker import add_expense, list_expenses, show_total, show_category_summary

MENU_OPTIONS = {
    "1": ("Add Expense", add_expense),
    "2": ("View All Expenses", list_expenses),
    "3": ("Total Spending", show_total),
    "4": ("Category Summary", show_category_summary),
}

MENU_TEXT = """
==============================
 Personal Expense Tracker
==============================
1) Add Expense
2) View All Expenses
3) Total Spending
4) Category Summary
5) Save & Exit
==============================
"""


def show_menu() -> None:
    """Display the menu."""
    print(MENU_TEXT)


def execute_action(choice: str, expenses: list[dict]) -> bool:
    """Execute the selected action. Returns True to exit, False to continue."""
    if choice in MENU_OPTIONS:
        _, action = MENU_OPTIONS[choice]
        action(expenses)
        return False
    elif choice == "5":
        save_expenses(expenses)
        print("exiting...")
        return True
    else:
        print("Invalid choice. Please select 1-5.")
        return False


def main() -> None:
    """Main application loop."""
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("select an option (1-5): ").strip()
        if execute_action(choice, expenses):
            break


if __name__ == "__main__":
    main()