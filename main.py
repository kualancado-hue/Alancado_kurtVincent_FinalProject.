import json, pathlib
from datetime import datetime
from dataclasses import dataclass, asdict
from collections import Counter

DATA_FILE = pathlib.Path("budget_data.json")

@dataclass
class Transaction:
    amount: float
    category: str
    description: str
    type: str 
    date: str = None

    def __post_init__(self):
        if not self.date: self.date = datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        s = "+" if self.type == "income" else "-"
        return f"{self.date} | {s}${self.amount:.2f} | {self.category} | {self.description}"

class BudgetTracker:
    def __init__(self):
        self.transactions = []
        if DATA_FILE.exists():
            with open(DATA_FILE, 'r') as f:
                self.transactions = [Transaction(**t) for t in json.load(f)]

    def save(self):
        with open(DATA_FILE, 'w') as f:
            json.dump([asdict(t) for t in self.transactions], f, indent=4)

    def view(self, filter_type=None):
        ts = [t for t in self.transactions if not filter_type or t.type == filter_type]
        if not ts: return print("\nNo transactions found.")
        
        print(f"\n{'DATE':<12} {'TYPE':<8} {'AMOUNT':<10} {'CATEGORY':<12} {'DESC'}\n" + "="*60)
        for t in ts:
            s = "+" if t.type == "income" else "-"
            print(f"{t.date:<12} {t.type:<8} {s}${t.amount:<9.2f} {t.category:<12} {t.description}")

    def summary(self):
        inc = sum(t.amount for t in self.transactions if t.type == "income")
        exp = sum(t.amount for t in self.transactions if t.type == "expense")
        cats = Counter({t.category: 0 for t in self.transactions if t.type == "expense"})
        for t in self.transactions:
            if t.type == "expense": cats[t.category] += t.amount

        print(f"\nIncome: +${inc:.2f} | Expenses: -${exp:.2f} | Balance: ${inc-exp:.2f}")
        for cat, amt in sorted(cats.items(), key=lambda x: x[1], reverse=True):
            print(f"  {cat:<15} ${amt:.2f} ({(amt/exp*100):.1f}%)")

def main():
    bt = BudgetTracker()
    menu = "Choice:"
    print("1: Add Income") 
    print("2: Add Expense") 
    print("3: View All") 
    print("4: View Income")
    print("5: View Expense") 
    print("6: Summary") 
    print("7: Search") 
    print("8: Delete") 
    print("9: Exit") 
    
    while True:
        choice = input(menu)
        try:
            if choice in ["1", "2"]:
                t_type = "income" if choice == "1" else "expense"
                bt.transactions.append(Transaction(
                    float(input("Amount: $")), 
                    input("Category: "), 
                    input("Description: "), 
                    t_type))
                bt.save()
            elif choice in ["3", "4", "5"]:
                f = {"3": None, "4": "income", "5": "expense"}[choice]
                bt.view(f)
            elif choice == "6":
                bt.summary()
            elif choice == "7":
                kw = input("Keyword: ").lower()
                for t in bt.transactions:
                    if kw in str(t).lower(): print(t)
            elif choice == "8":
                idx = int(input("Index to delete: "))
                if 0 <= idx < len(bt.transactions):
                    print(f"Deleted: {bt.transactions.pop(idx)}")
                    bt.save()
            elif choice == "9":
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
         main()