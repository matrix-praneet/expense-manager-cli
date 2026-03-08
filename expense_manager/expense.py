# This file defines what an Expense object looks like

class Expense:

    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

# bcz json file cannot store objects directly they store dictionaries

    def to_dict(self):
        return {
            "amount":self.amount,
            "category":self.category,
            "description":self.description,
            "date":self.date
        }