import os
from user import UserManager
from finance import FinanceManager
from report import ReportGenerator
from storage import Storage
from utils import validate_amount, clear_screen

def main():
    clear_screen()
    print("欢迎使用个人财务管理系统")
    
    # 初始化存储与管理器
    storage = Storage()
    user_manager = UserManager(storage)
    finance_manager = FinanceManager(storage)
    report_generator = ReportGenerator(finance_manager)

    # 用户登录或注册
    user = None
    while not user:
        action = input("请输入 '1' 登录，'2' 注册：")
        if action == '1':
            user = user_manager.login()
        elif action == '2':
            user = user_manager.register()

    clear_screen()
    print(f"欢迎回来, {user.username}!")
    
    # 主菜单
    while True:
        print("\n请选择操作:")
        print("1. 记录收入或支出")
        print("2. 查看财务状况")
        print("3. 查看报表")
        print("4. 退出")
        
        choice = input("请输入选项: ")
        
        if choice == '1':
            finance_manager.record_transaction(user)
        elif choice == '2':
            finance_manager.view_balance(user)
        elif choice == '3':
            report_generator.generate_report(user)
        elif choice == '4':
            print("感谢使用本系统，再见！")
            break
        else:
            print("无效选项，请重新输入。")

if __name__ == '__main__':
    main()
