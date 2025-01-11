from datetime import datetime
from utils import validate_amount

class FinanceManager:
    def __init__(self, storage):
        self.storage = storage

    def record_transaction(self, user):
        print("\n选择操作:")
        print("1. 记录收入")
        print("2. 记录支出")
        
        choice = input("请输入选项: ")
        if choice not in ['1', '2']:
            print("无效选项。")
            return

        transaction_type = "收入" if choice == '1' else "支出"
        amount = float(input(f"请输入{transaction_type}金额: "))
        amount = validate_amount(amount)
        category = input("请输入类别 (如：餐饮，娱乐，工资): ")
        date = input(f"请输入日期 (默认: {datetime.now().strftime('%Y-%m-%d')}): ") or datetime.now().strftime('%Y-%m-%d')
        notes = input("请输入备注（可选）: ")

        self.storage.save_transaction(user.username, transaction_type, amount, category, date, notes)
        print(f"{transaction_type}记录已成功保存!")

    def view_balance(self, user):
        balance, total_income, total_expense = self.storage.get_balance(user.username)
        print(f"\n账户余额: {balance}元")
        print(f"总收入: {total_income}元")
        print(f"总支出: {total_expense}元")

