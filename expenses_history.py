import json


def load_expenses():
    try:
        with open("expenses.json","r")as file:
            expenses_history = json.load(file)
        return expenses_history
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    with open("expenses.json","w")as file:
        json.dump(expenses,file,indent=3)
