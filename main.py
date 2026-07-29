from datetime import datetime
from expenses_history import save_expenses, load_expenses

expenses =load_expenses()



def add_expense():

    current_time = datetime.now().strftime("%Y-%m-%d  %I:%M %p")
    category = input("Enter the category: ").strip()

    while not category:
        print("Please Enter a category!")
        category = input("Enter the category: ").strip()

    while True:
        try:
            amount = float(input("Enter the Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break
        except ValueError:
            print("Please enter a valid number.")
            

    expense = {
        "category" : category,
        "amount" : amount,
        "date" : current_time
    }
    expenses.append(expense)
    print("Expense Added Succesfully!")
    save_expenses(expenses)



def view_expenses():

    for i,expense in enumerate (expenses,start=1):
        print(f"{i}. {expense["category"]} - ₹{expense["amount"]}\n{expense["date"]}")



def total_expenses():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total Expenses: ₹{total}")



def delete_expense():
    for i,expense in enumerate (expenses,start=1):
        print(f"{i}. {expense["category"]} - {expense["amount"]}")

    while True:
        try:
            delete = int(input("Which one do you wanna delete?: "))

            if 1<= delete <= len(expenses):
                    expenses.pop(delete - 1)
                    print("Expense deleted Succesfully.")
                    break
            else:
                print("Please enter a valid expense number.")
                continue
  
        except ValueError:
            print("Invalid Expense number.")
            continue

    save_expenses(expenses)

    


def main():
    while True:
        print("\n=====Expense Tracker=====")
        print("1.Add Expense")
        print("2.View Expenses")
        print("3.Total Expenses")
        print("4.Delete Expense")
        print("5.Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            add_expense()
            


        elif choice == 2:
            if not expenses:
                print("No expenses found!")
                continue
            view_expenses()


        elif choice == 3:
            total_expenses()
            

        elif choice == 4:
            if not expenses:
                print("No Expenses to delete!")
                continue
            delete_expense()

            
        elif choice == 5:
            print("Goodbye!")
            break


        else:
            print("Invalid Choice!")




if __name__ == "__main__":
    main()
