#This code analyzes a user's expenses and determines what the highest and lowest expenses are.
from functools import reduce

def main():
    # Function to get expenses from the user
    def get_expenses():
        expenses = []
        while True:
            expense_type = input("Enter the type of expense (or 'done' to finish): ")
            if expense_type.lower() == 'done':
                break
            try:
                amount = float(input(f"Enter the amount for {expense_type}: "))
                expenses.append((expense_type, amount))
            except ValueError:
                print("Please enter a valid amount.")
        return expenses

    # Function to find the total expense
    def calculate_total(expenses):
        return reduce(lambda acc, exp: acc + exp[1], expenses, 0)

    # Function to find the highest expense
    def find_highest(expenses):
        return reduce(lambda acc, exp: acc if acc[1] > exp[1] else exp, expenses)

    # Function to find the lowest expense
    def find_lowest(expenses):
        return reduce(lambda acc, exp: acc if acc[1] < exp[1] else exp, expenses)

    # Get expenses from the user
    expenses = get_expenses()

    if not expenses:
        print("No expenses entered.")
        return

    # Calculate total, highest, and lowest expenses
    total_expense = calculate_total(expenses)
    highest_expense = find_highest(expenses)
    lowest_expense = find_lowest(expenses)

    # Display results
    print(f"\nTotal Expense: ${total_expense:.2f}")
    print(f"Highest Expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest Expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")


if __name__ == "__main__":
    main()