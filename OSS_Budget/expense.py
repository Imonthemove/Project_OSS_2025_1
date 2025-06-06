class Expense:
    def __init__(self, date, category, description, amount_krw, amount_usd=0):
        self.date = date
        self.category = category
        self.description = description
        self.amount_krw = amount_krw
        self.amount_usd = amount_usd

    def __str__(self):
        usd_display = f" (${self.amount_usd:.2f})" if self.amount_usd else ""
        return f"[{self.date}] {self.category} - {self.description}: {self.amount_krw}원{usd_display}"
