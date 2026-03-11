from expense import Expense
from storage import load_expenses, save_expenses

expenses = load_expenses()

while True:  
  
  print("1. Add Expense")
  print("2. View Expenses")
  print("3. Delete Expense")
  print("4. Summary")
  print("5. Exit")

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
   if not expenses:
     print("No expenses recorded.")
   for expense in expenses:
       print("Expense:", i)
       print("Amount:", expense["amount"])
       print("Category:", expense["category"])
       print("Description:", expense["description"])
       print("Date:", expense["date"])
       print("--------------------")

  elif choice == "3":
   for i, expense in enumerate(expenses):
      print(i, expense)
      index = int(input("Enter the number of the expense to delete: "))
      if index < 0 or index >= len(expenses):
        print("Invalid index. Please try again.")
      else:
        expenses.pop(index)
        save_expenses(expenses)
        print("Expense deleted successfully.")

  elif choice == "4":
    total = 0
    for expense in expenses:
      total += int(expense["amount"])

    print("Total Expenses:", total)
        

  elif choice == "5":
    print("Exiting the program.")   
    break

