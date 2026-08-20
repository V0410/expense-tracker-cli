import sqlite3
from datetime import datetime

connection = sqlite3.connect("expenses.db")
cursor = connection.cursor()



def display_expense(expense):
    print(f"ID : {expense[0]}")
    print(f"Name : {expense[1]}")
    print(f"Amount : {expense[2]}")
    print(f"Category : {expense[3]}")
    print(f"Date : {expense[4]}")
    print("--------------------------")


def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        amount REAL,
        category TEXT,
        date TEXT
        )
        """)
    connection.commit()
    


def add_expense():

    name = input("Enter expense name: ")

    while True:
        try:    
            amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Please enter amount only, nothing else!")
            

    category = input("Enter expense category: ")
    
    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO expenses
        (name, amount, category, date)
        VALUES
        (?, ?, ?, ?)
        """,(name, amount, category, date))
    connection.commit()


def view_expenses():

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    if not expenses:
        print("No Expenses Found.")
        return
    
    for expense in expenses:
        display_expense(expense)


def update_expense():
    while True:
        try:
            expense_id = int(input("Enter the ID of the expense you want to update: "))
            break
        except ValueError:
            print("Please Enter the ID, not anything else!")

    print("Current Expense:")
    cursor.execute("""
        SELECT *
        FROM expenses
        WHERE id = ?
        """,(expense_id,))

    expense = cursor.fetchone()
    if expense is None:
        print("No Expense Found")
        return

    display_expense(expense)

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Amount")
    print("3. Category")
    print("4. Cancel")
    choice = (input("What do you want to update(1/2/3/4): "))

    if choice == "1":
        new_name = input("Enter the new Name: ")

        cursor.execute("""
            UPDATE expenses
            SET name = ?
            WHERE id = ?
            """,(new_name, expense_id))
        
        

    elif choice == "2":
        while True:
            try:
                new_amount = float(input("Enter the new amount: "))
                break
            except ValueError:
                print("Please enter amount only, nothing else!")

        cursor.execute("""
            UPDATE expenses
            SET amount = ?
            WHERE id = ?
            """,(new_amount, expense_id))


    elif choice == "3":
        new_category = input("Enter the new Category: ")

        cursor.execute("""
            UPDATE expenses
            SET category = ?
            WHERE id = ?
            """,(new_category, expense_id))
        

    elif choice == "4":
        print("Update cancelled")
        return

    else:
        print("Invalid Choice!")
        return

    
    connection.commit()
    print("Expense Updated Successfully.")



def monthly_total():
    month = input("Enter month (YYYY-MM): ")
    cursor.execute("""
        SELECT sum(amount) 
        FROM expenses
        WHERE date LIKE ?
        """,(f"{month}%",))

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print(f"Total Expenses for {month}: ₹{total}")



def delete_expense():
    while True:
        try:
            expense_id = int(input("Enter the ID of the expense you want to delete: "))
            break
        except ValueError:
            print("Please Enter the ID, not anything else!")

    cursor.execute("""
        DELETE FROM expenses
        WHERE id = ?
        """,(expense_id, ))

    if cursor.rowcount == 0:
        print("Expense Not Found.")
    else:
        print("Expense Deleted Successfully.")

    connection.commit()


def search_expense():
    search_term = input("Enter expense name to search: ")

    cursor.execute("""
        SELECT *
        FROM expenses
        WHERE name LIKE ?
        """,(f"%{search_term}%",))

    expenses = cursor.fetchall()

    if not expenses:
        print("No Expense Found.")
    else:
        for expense in expenses:
                display_expense(expense)



def category_filter():
    category = input("Enter category: ")

    cursor.execute("""
        SELECT *
        FROM expenses
        WHERE category = ?
        """,(category,))

    expenses = cursor.fetchall()

    if not expenses:
        print("No Expenses Found.")
    else:
        for expense in expenses:
                display_expense(expense)
    


def main():
    while True:
        print("\n====================")
        print("   Expense Tracker   ")
        print("====================")
        print()
        print("1.Add Expense")
        print("2.View Expenses")
        print("3.Update Expense")
        print("4.Monthly Total")
        print("5.Delete Expense")
        print("6.Search Expense")
        print("7.Category Filter")
        print("8.Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            add_expense()
            
        elif choice == 2:
            view_expenses()

        elif choice == 3:
            update_expense()

        elif choice == 4:
            monthly_total()
            
        elif choice == 5:
            delete_expense()

        elif choice == 6:
            search_expense()

        elif choice == 7:
            category_filter()
            
        elif choice == 8:
            print("Goodbye!")
            break

        else:
            print("Invalid Choice!")




if __name__ == "__main__":
    create_table()
    main()
    connection.close()
