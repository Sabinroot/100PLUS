import time
import requests

url = "https://krivchenkov6.tback.zendo.cloud/api/v1/register"
url_auf = "https://krivchenkov6.tback.zendo.cloud/api/v1/login"
url_acc = "https://krivchenkov6.tback.zendo.cloud/api/v1/user/finance/accounts"
url_money_up = "https://krivchenkov6.tback.zendo.cloud/api/v1/admin/finance/operations/user-transfer"
url_game_activation= "https://krivchenkov6.tback.zendo.cloud/api/v1/buy/game-activation"

inviter = "t1000"
admin_login = "admin"
password_admin = "Xeb2Liv8Fym7Pit8Zaf9"


password = "123456"
headers =  register_headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, /'
        }

# Шаг 1. Создаем пользователя.
class UserGenerator:  # Гениратор пользователей. Нужно настраивать
    def generate_login(self, index):
        return "t1000" + str(1 + index) #настрой окончание  логина

    def generate_users(self, count):
        for i in range(count):
            login = self.generate_login(i)
            self.create_user(login)

    def create_user(self, login):
        data = {
            "password": "123456",
            "username": login,
            "sponsor_username": inviter,
            'password_confirmation':"123456",
            "email": login + "@gmail.com",
            "agreement": "true",
            "has_sponsor": 1
        }
        print("шаг 1 Создание пользователя")
        post_registr = requests.post(url=url, headers=register_headers, json=data)
        if post_registr.status_code == 201:
            print(post_registr.status_code)
            print(f"User--- {login} ---created successfully")
        else:
            print(f"Failed to create user {login}")
            print(post_registr.status_code)
            print(post_registr.json())



# Использование класса UserGenerator для создания 10 пользователей
generator = UserGenerator()
generator.generate_users(1)



