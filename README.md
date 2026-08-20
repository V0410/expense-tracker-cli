# 💰 Expense Tracker CLI

A command-line expense tracking application built with Python and SQLite. It allows users to add, view, update, delete, search, and filter expenses directly from the terminal.

Expense data is stored persistently in a local SQLite database, so records remain available between program executions.

---

## ✨ Features

* ✅ Add new expenses
* ✅ View all saved expenses
* ✅ Update expense details
* ✅ Delete individual expenses
* ✅ Search expenses by name
* ✅ Calculate monthly expense totals
* ✅ Filter expenses by category
* ✅ Automatically record the current date
* ✅ Input validation for user-friendly interaction
* ✅ Persistent data storage using SQLite
* ✅ Simple menu-driven command-line interface

---

## 🛠️ Technologies Used

* Python 3
* SQLite
* Python Standard Library

  * `sqlite3`
  * `datetime`

No external Python packages are required.

---

## 📂 Project Structure

```text
expense-tracker-cli/
│
├── main.py          # Main application logic and CLI menu
├── expenses.db      # SQLite database (generated automatically)
├── .gitignore       # Files excluded from version control
└── README.md        # Project documentation
```

> `expenses.db` is generated automatically when the application is first run and is excluded from Git.

---

## 📋 Requirements

* Python 3.10 or later

No external libraries are required.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/V0410/expense-tracker-cli.git
cd expense-tracker-cli
```

### 2. Run the application

```bash
python main.py
```

The SQLite database will be created automatically if it does not already exist.

---

## 📖 Menu

```text
====================
   Expense Tracker
====================

1. Add Expense
2. View Expenses
3. Update Expense
4. Monthly Total
5. Delete Expense
6. Search Expense
7. Category Filter
8. Exit
```

---

## 📊 Expense Information

Each expense stores the following information:

* **ID** — Automatically generated unique identifier
* **Name** — Name of the expense
* **Amount** — Expense amount
* **Category** — Expense category
* **Date** — Automatically recorded date in `YYYY-MM-DD` format

---

## 📸 Example

```text
====================
   Expense Tracker
====================

1. Add Expense
2. View Expenses
3. Update Expense
4. Monthly Total
5. Delete Expense
6. Search Expense
7. Category Filter
8. Exit

Choose an option: 1

Enter expense name: Groceries
Enter expense amount: 550
Enter expense category: Food

Expense added successfully.
```

Example expense record:

```text
ID : 1
Name : Groceries
Amount : 550.0
Category : Food
Date : 2026-08-20
```

---

## ⚠️ Error Handling

The application handles common user input errors, including:

* Invalid menu choices
* Invalid expense amounts
* Invalid expense IDs
* Attempts to update or delete an expense that does not exist
* Empty expense results when viewing, searching, or filtering

---

## 🗄️ SQLite Database

The application uses SQLite through Python's built-in `sqlite3` module.

The database contains an `expenses` table with the following structure:

```text
expenses
├── id
├── name
├── amount
├── category
└── date
```

SQL operations practiced in this project include:

* `CREATE TABLE`
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`
* `WHERE`
* `LIKE`
* `SUM`

Parameterized SQL queries are used when inserting and modifying user-provided data.

---

## 📚 What I Learned

This project helped me practice:

* Python functions
* Exception handling
* Loops and conditional logic
* User input validation
* CRUD operations
* SQL fundamentals
* SQLite database integration with Python
* Parameterized SQL queries
* Fetching database records with `fetchone()` and `fetchall()`
* Aggregate queries using `SUM()`
* Searching with `LIKE`
* Filtering data with `WHERE`
* Menu-driven CLI application design
* Refactoring repeated code into reusable functions
* Git and GitHub workflow

---

## 🔄 Project Evolution

This project originally used JSON file storage.

It was later upgraded to SQLite to provide a more structured and scalable approach to persistent data storage.

```text
JSON File Storage
       ↓
SQLite Database
```

This migration also provided practical experience with SQL and database-driven application design.

---

## 🚀 Future Improvements

Possible future improvements include:

* Flask web interface
* REST API
* User authentication
* CSV export
* Docker containerization
* PostgreSQL database
* Cloud deployment
* Automated testing

---

## 🤝 Contributing

This project was created for learning purposes, but suggestions and improvements are welcome.

---

## 📄 License

This project is intended for educational purposes.

---

## 👨‍💻 Author

**Vansh Gokhale**

Aspiring Python Backend & Cloud Engineer
