import csv
from datetime import datetime

# File to store expenses
FILENAME = "expenses.csv"

# Load existing data or create new storage
def load_data():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

# Save data to a file
def save_data(expenses):
    with open(FILENAME, "w", newline="") as file:
        fieldnames = ["date", "amount", "category", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

# Input new expense
def add_expense(expenses):
    print("\n=== Add New Expense ===")
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
    date = date if date else datetime.now().strftime("%Y-%m-%d")
    try:
        amount = float(input("Enter the amount (e.g., 100.50): "))
    except ValueError:
        print("⚠️ Invalid amount. Please enter a numeric value.")
        return
    category = input("Enter the category (e.g., Food, Rent, Entertainment): ").strip()
    description = input("Enter a brief description: ").strip()
    
    expenses.append({"date": date, "amount": amount, "category": category, "description": description})
    save_data(expenses)
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses(expenses):
    print("\n=== All Recorded Expenses ===")
    if not expenses:
        print("No expenses recorded yet. Start adding some!")
        return
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['date']} - {expense['category']} - {expense['description']} - ${float(expense['amount']):.2f}")
    print("")

# Display category-wise summary
def summary_by_category(expenses):
    print("\n=== Summary by Category ===")
    if not expenses:
        print("No expenses recorded yet to analyze.")
        return
    category_summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])
        category_summary[category] = category_summary.get(category, 0) + amount
    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")
    print("")

# Display monthly summary
def monthly_summary(expenses):
    print("\n=== Monthly Expense Summary ===")
    if not expenses:
        print("No expenses recorded yet to analyze.")
        return
    monthly_summary = {}
    for expense in expenses:
        month = expense["date"][:7]  # Extract YYYY-MM
        amount = float(expense["amount"])
        monthly_summary[month] = monthly_summary.get(month, 0) + amount
    for month, total in monthly_summary.items():
        print(f"{month}: ${total:.2f}")
    print("")

# Main menu
def main_menu():
    print("\n=== Expense Tracker ===")
    print("1️⃣ Add New Expense")
    print("2️⃣ View All Expenses")
    print("3️⃣ Category-wise Summary")
    print("4️⃣ Monthly Summary")
    print("5️⃣ Exit")
    return input("Choose an option (1-5): ")

# Main function
def main():
    expenses = load_data()
    print("💰 Welcome to Expense Tracker 💰")
    while True:
        choice = main_menu()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary_by_category(expenses)
        elif choice == "4":
            monthly_summary(expenses)
        elif choice == "5":
            print("👋 Goodbye! Keep tracking your expenses wisely!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
