from expen import Expense
def main():
   expense_file_path="expense.csv"

   expense = userinput()

   save_expense_to_file(expense, expense_file_path)

   summarise_expense(expense_file_path)
   


 #User input expense.

def userinput():
    expense_name= input("Enter expense name: ")
    expense_amount= float(input("Enter expense amount: "))
    
    expense_categories = [
        "🍔Food", 
        "🏠Home", 
        "💼Work", 
        "🕺🏽Fun",
        "🤠Misc",

        ] 
    
    while True:
        print("Select a category please: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")

        value_range=f"[1-{len(expense_categories)}]"
        user_selected= int(input(f"Enter a category number {value_range}: ")) -1

        
        #Added -1 as we added 1 beforehand so reset back to normal index numbers where it starts from 0
        if user_selected in range(len(expense_categories)):
         selected_category=expense_categories[user_selected]
         new_expense=Expense(name=expense_name,category=selected_category,amount=expense_amount)
         return new_expense
        else:
           print("Invalid input please try again")



 


#Save to csv file

def save_expense_to_file(expense:Expense, expense_file_path):
   with open(expense_file_path, "a") as f:
      #"a" means append which means not to over]write this file jus add on to
      f.write(f"{expense.name},{expense.amount},{expense.category}\n")
   
#Read that csv file
 

def summarise_expense(expense_file_path):
   with open(expense_file_path, "r") as f:
      #r is read only
      lines= f.readlines()
      for line in lines:
         print(line) 
         

if __name__=="__main__":
    main()