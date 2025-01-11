import json
import hashlib
from storage import Storage

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self, storage):
        self.storage = storage
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self):
        while True:
            username = input("请输入用户名: ")
            if self.storage.user_exists(username):
                print("用户名已存在，请重新输入。")
                continue
            password = input("请输入密码: ")
            hashed_password = self.hash_password(password)
            self.storage.save_user(username, hashed_password)
            print(f"用户 {username} 注册成功！")
            return User(username, password)
    
    def login(self):
        while True:
            username = input("请输入用户名: ")
            password = input("请输入密码: ")
            hashed_password = self.hash_password(password)
            if self.storage.check_user_credentials(username, hashed_password):
                print(f"欢迎回来，{username}!")
                return User(username, password)
            else:
                print("用户名或密码错误，请重新输入。")
