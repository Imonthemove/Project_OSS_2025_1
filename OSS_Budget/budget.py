import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.special_days = set([
            "01-01",  # 새해
            "02-14",  # 발렌타인데이
            "06-06",  # 현충일
            "06=25",  # 내 생일
            "12-25",  # 크리스마스
        ])

    def is_special_day(self):
        today_str = datetime.date.today().strftime("%m-%d")
        return today_str in self.special_days

    def add_special_day(self, date_str):
        if len(date_str) != 5 or date_str[2] != '-' or not date_str.replace("-", "").isdigit():
            print("잘못된 형식입니다. MM-DD 형식으로 입력해주세요.\n")
            return
        self.special_days.add(date_str)
        print(f"{date_str} 기념일이 추가되었습니다!\n")

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
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
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

