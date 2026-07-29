# 💰 Expense Tracker CLI

A command-line expense tracking application built with Python that allows users to record, view, calculate, and manage their daily expenses. All expense data is stored locally in a JSON file, ensuring that records persist between program executions.

---

## ✨ Features

- ✅ Add new expenses
- ✅ View all saved expenses
- ✅ Calculate total expenses
- ✅ Delete individual expenses
- ✅ Automatically save expenses to a JSON file
- ✅ Automatically load existing expenses when the application starts
- ✅ Input validation for user-friendly interaction
- ✅ Simple menu-driven command-line interface

---

## 🛠️ Technologies Used

- Python 3
- JSON
- Python Standard Library (`json`, `datetime`)

---

## 📂 Project Structure

```text
expense-tracker-cli/
│
├── main.py                # Main menu and program flow
├── expenses_history.py    # Handles expense storage and management
├── expenses.json          # Stores expense data (generated automatically)
└── README.md
```

---

## 📋 Requirements

- Python 3.10 or later

> No external libraries are required for this project.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/expense-tracker-cli.git

cd expense-tracker-cli
```

---

## ▶️ Running the Application

```bash
python main.py
```

---

## 📖 Menu

```text
======== Expense Tracker ========

1. Add Expense
2. View Expenses
3. Calculate Total Expenses
4. Delete Expense
5. Exit
```

---

## 📸 Example Output

```text
Expense Added Successfully!

Title   : Groceries
Amount  : ₹550
Date    : 2026-07-29
```

---

## ⚠️ Error Handling

The application handles common user input errors, including:

- Invalid menu choices
- Invalid expense amount
- Empty expense list
- Invalid expense number
- Missing or corrupted JSON file

---

## 📚 What I Learned

This project helped me practice:

- Working with JSON files
- File handling in Python
- CRUD (Create, Read, Update, Delete) operations
- Exception handling
- Functions
- Lists and dictionaries
- Modular programming
- Building menu-driven CLI applications

---

## 🚀 Future Improvements

- SQLite database integration
- Monthly expense reports
- Expense categories
- Search and filter expenses
- Export data to CSV
- Flask REST API
- User authentication
- Docker support
- AWS deployment

---

## 🤝 Contributing

This project was created for learning purposes, but suggestions and improvements are always welcome.

---

## 📄 License

This project is intended for educational purposes.

---

## 👨‍💻 Author

**Vansh Gokhale**

Aspiring Python Backend & Cloud Engineer