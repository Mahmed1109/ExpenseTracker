from expen import Expense
import calendar
import datetime

def main():
    expense_file_path = "expense.csv"
    budget = 2000

    expenses = userinput()

    # Loop through the list of expenses and save each one individually
    for expense in expenses:
        save_expense_to_file(expense, expense_file_path)

    summarise_expense(expense_file_path, budget)



 #User input expense.

def userinput():
    expense_categories = [
        "🍔Food", 
        "🏠Home", 
        "💼Work", 
        "🕺🏽Fun",
        "🤠Misc",
    ]

    expenses = []

    while True:
        print("\n📝 Enter a new expense:")
        expense_name = input("Enter expense name: ")

        try:
            expense_amount = float(input("Enter expense amount: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        # Category selection loop
        while True:
            print("Select a category:")
            for i, category_name in enumerate(expense_categories):
                print(f"{i+1}. {category_name}")

            value_range = f"[1-{len(expense_categories)}]"
            try:
                user_selected = int(input(f"Enter a category number {value_range}: ")) - 1
            except ValueError:
                print("⚠️ Invalid input, must be a number.")
                continue

            if user_selected in range(len(expense_categories)):
                selected_category = expense_categories[user_selected]
                break
            else:
                print("⚠️ Invalid category, please try again.")

        # Create and store expense
        new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
        expenses.append(new_expense)

        # Ask if they want to add another
        more = input("Add another expense? (y/n): ").strip().lower()
        if more != "y":
            break

    return expenses

 


#Save to csv file

def save_expense_to_file(expense:Expense, expense_file_path):
   with open(expense_file_path, "a") as f:
      #"a" means append which means not to over]write this file jus add on to
      f.write(f"{expense.name},{expense.amount},{expense.category}\n")
   
#Read that csv file
 

def summarise_expense(expense_file_path,budget):
    print(f"🎯 Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)


    amount_by_category={}
    for expense in expenses:
       key=expense.category
       if key in amount_by_category:
          amount_by_category[key]+=expense.amount
       else:
          amount_by_category[key]=expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")
    

    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: £{total_spent:.2f}")

    remaining_budget= budget - total_spent
    print(f"Budget remaining: £{remaining_budget:.2f}")


    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print((f"👉 Budget Per Day: ${daily_budget:.2f}"))




    # Only print once
    print(expenses)
if __name__=="__main__":
    main()