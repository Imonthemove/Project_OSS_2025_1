import tkinter as tk
from tkinter import simpledialog, messagebox  # 새로 추가

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")  # 높이 살짝 늘림

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 구성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', 'ERA']  # ERA 버튼 추가
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == "ERA":
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 16),
                        bg="#d0f0c0",
                        command=self.calculate_era
                    )
                else:
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 18),
                        command=lambda ch=char: self.on_click(ch)
                    )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def calculate_era(self):
        try:
            earned_runs = simpledialog.askfloat("평균자책점 계산", "자책점 (earned runs)을 입력하세요:")
            innings = simpledialog.askfloat("평균자책점 계산", "투구 이닝 (innings pitched)을 입력하세요:")

            if innings is None or innings == 0:
                messagebox.showerror("오류", "투구 이닝은 0보다 커야 합니다.")
                return

            era = (earned_runs * 9) / innings
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, f"ERA: {era:.2f}")
        except Exception as e:
            messagebox.showerror("에러", f"계산 중 오류 발생: {e}")
