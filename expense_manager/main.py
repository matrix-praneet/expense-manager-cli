from expense import Expense
from storage import load_expenses, save_expenses

expenses = load_expenses()

while True:  
  
  print("1. Add Expense")
  print("2. View Expenses")
  print("3. Exit")

  choice = input("Choose an option: ")
 
  if choice == "1":
   
   amount = input("Enter the amount: ")
   category = input("Enter the category: ")
   description = input("Enter the description: ")
   date = input("Enter the date (DD-MM-YYYY: ")

   new_expense = Expense(amount, category, description, date)
   expense_dict = new_expense.to_dict()
   expenses.append(expense_dict)

   save_expenses(expenses)

  elif choice == "2":
   for expense in expenses:
       print("Amount:", expense["amount"])
       print("Category:", expense["category"])
       print("Description:", expense["description"])
       print("Date:", expense["date"])
       print("--------------------")

  elif choice == "3":
    print("Exiting the program.")   
    break

