import matplotlib.pyplot as plt

class ReportGenerator:
    def __init__(self, finance_manager):
        self.finance_manager = finance_manager
    
    def generate_report(self, user):
        print("\n选择报表类型:")
        print("1. 按月财务报表")
        print("2. 按类别财务报表")
        
        choice = input("请输入选项: ")
        if choice == '1':
            self.generate_monthly_report(user)
        elif choice == '2':
            self.generate_category_report(user)
        else:
            print("无效选项，请重新选择。")
    
    def generate_monthly_report(self, user):
        transactions = self.finance_manager.storage.get_transactions(user.username)
        monthly_data = {}
        for transaction in transactions:
            month = transaction['date'][:7]  # 按月统计
            if month not in monthly_data:
                monthly_data[month] = {'收入': 0, '支出': 0}
            if transaction['type'] == '收入':
                monthly_data[month]['收入'] += transaction['amount']
            else:
                monthly_data[month]['支出'] += transaction['amount']
        
        months = list(monthly_data.keys())
        income = [monthly_data[m]['收入'] for m in months]
        expense = [monthly_data[m]['支出'] for m in months]
        
        plt.figure(figsize=(10, 6))
        plt.bar(months, income, label='收入')
        plt.bar(months, expense, label='支出', bottom=income)
        plt.xlabel('月份')
        plt.ylabel('金额')
        plt.title('按月财务报表')
        plt.legend()
        plt.show()

    def generate_category_report(self, user):
        transactions = self.finance_manager.storage.get_transactions(user.username)
        category_data = {}
        for transaction in transactions:
            if transaction['category'] not in category_data:
                category_data[transaction['category']] = {'收入': 0, '支出': 0}
            if transaction['type'] == '收入':
                category_data[transaction['category']]['收入'] += transaction['amount']
            else:
                category_data[transaction['category']]['支出'] += transaction['amount']
        
        categories = list(category_data.keys())
        income = [category_data[c]['收入'] for c in categories]
        expense = [category_data[c]['支出'] for c in categories]
        
        plt.figure(figsize=(10, 6))
        plt.bar(categories, income, label='收入')
        plt.bar(categories, expense, label='支出', bottom=income)
        plt.xlabel('类别')
        plt.ylabel('金额')
        plt.title('按类别财务报表')
        plt.legend()
        plt.show()

