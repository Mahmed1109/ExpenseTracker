from expen import Expense
def main():
   expense=userinput()
   pass
 #User input expense.

def userinput():
    expensename= input("Enter expense name: ")
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
        user_selected=int (input(f"Enter a category number {value_range}: ")) -1

        
        #Added -1 as we added 1 beforehand so reset back to normal index numbers where it starts from 0
        if user_selected in range(len(expense_categories)):

         new_expense=Expense()
        else:
           print("Invalid input please try again")


    





    #Save it to a csv file.



    #Read file and summarise expenses.

if __name__=="__main__":
    main()