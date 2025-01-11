import os
def validate_amount(amount):
    if amount <= 0:
        print("金额必须为正数。")
        return 0.0
    return amount

def clear_screen():
    # 清屏操作
    os.system('cls' if os.name == 'nt' else 'clear')
