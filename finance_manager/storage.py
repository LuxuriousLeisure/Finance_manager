import json
import os
from datetime import datetime

class Storage:
    def __init__(self):
        self.data_dir = './data'
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.users_file = os.path.join(self.data_dir, 'users.json')
        self.transactions_file = os.path.join(self.data_dir, 'finance.json')
        self.load_data()
    
    def load_data(self):
        self.users = self.load_json(self.users_file)
        self.transactions = self.load_json(self.transactions_file)
    
    def load_json(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def save_data(self):
        self.save_json(self.users_file, self.users)
        self.save_json(self.transactions_file, self.transactions)
    
    def save_json(self, filename, data):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def user_exists(self, username):
        return any(user['username'] == username for user in self.users)
    
    def save_user(self, username, hashed_password):
        self.users.append({'username': username, 'password': hashed_password})
        self.save_data()
    
    def check_user_credentials(self, username, hashed_password):
        return any(user['username'] == username and user['password'] == hashed_password for user in self.users)
    
    def save_transaction(self, username, transaction_type, amount, category, date, notes):
        transaction = {
            'username': username,
            'type': transaction_type,
            'amount': amount,
            'category': category,
            'date': date,
            'notes': notes
        }
        self.transactions.append(transaction)
        self.save_data()
    
    def get_balance(self, username):
        balance = 0
        total_income = 0
        total_expense = 0
        for transaction in self.transactions:
            if transaction['username'] == username:
                if transaction['type'] == '收入':
                    total_income += transaction['amount']
                else:
                    total_expense += transaction['amount']
        balance = total_income - total_expense
        return balance, total_income, total_expense
    
    def get_transactions(self, username):
        return [transaction for transaction in self.transactions if transaction['username'] == username]
