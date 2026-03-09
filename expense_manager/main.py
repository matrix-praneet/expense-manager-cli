from expense import Expense
from storage import load_expenses, save_expenses

expenses = load_expenses()

print(expenses)

amount = input("Enter the amount: ")
category = input("Enter the category: ")
description = input("Enter the description: ")
date = input("Enter the date (DD-MM-YYYY: ")

new_expense = Expense(amount, category, description, date)
expense_dict = new_expense.to_dict()
expenses.append(expense_dict)

save_expenses(expenses)

