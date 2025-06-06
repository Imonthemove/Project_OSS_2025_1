import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.exchange_rate = 1350  # 고정 환율

    def add_expense(self, category, description, amount, currency):
        today = datetime.date.today().isoformat()

        if currency.lower() == "usd":
            amount_krw = int(amount * self.exchange_rate)
            expense = Expense(today, category, description, amount_krw, amount)
        else:
            expense = Expense(today, category, description, int(amount))

        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total_krw = sum(e.amount_krw for e in self.expenses)
        total_usd = sum(e.amount_usd for e in self.expenses)
        print(f"총 지출: {total_krw}원 (${total_usd:.2f})\n")
