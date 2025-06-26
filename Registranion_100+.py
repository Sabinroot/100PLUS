import time
import requests
url_1 = "https://krivchenkov6.tback.zendo.cloud"
url_register = "/api/v1/register"
url_auf = "/api/v1/login"
url_acc = "/api/v1/user/finance/accounts"
url_money = "/api/v1/admin/finance/operations/user-transfer"

admin_login ="admin"
admin_password = "123456"
inviter = "t10064"
password = "123456"
headers =  register_headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, /'
        }

# Шаг 1. Создаем пользователя.
class UserGenerator:  # Гениратор пользователей. Нужно настраивать
    def generate_login(self, index):
        return "t10064tt" + str(1 + index) #настрой окончание  логина

    def generate_users(self, count):
        for i in range(count):
            login = self.generate_login(i)
            self.create_user(login)

    def create_user(self, login):
        data = {
            "password": password,
            "username": login,
            "sponsor_username": inviter,
            'password_confirmation':"123456",
            "email": login + "@gmail.com",
            "agreement": "true",
            "country id":"690791",
            "has_sponsor": 1,
            "last_name": "Бонд",
            "first_name":"Джеймс",
            'phone':"+380636038450",
            "country_id":"690791"
        }
        
        print("шаг 1 Создание пользователя")
        post_registr = requests.post(url=url_1+url_register, headers=register_headers, json=data)
        if post_registr.status_code == 201:
            print(post_registr.status_code)
            print(f"User--- {login} ---created successfully")
        else:
            print(f"Failed to create user {login}")
            print(post_registr.status_code)
            print(post_registr.json())

# автооризация созданым юзером, узнаем id основного кошелька.
        body_1 = {

            "login": login,
            "password": password
        }

        print("Шаг 2.  Авторизация клиентом")
        print("____________________________________________________________________________________________")
        post_1 = requests.post(url=url_1+url_auf, headers=register_headers, json=body_1)
        print(post_1.status_code)
        print(post_1.json())

        if post_1.status_code == 200:
            print("статус код =", post_1.status_code)
            print("------------")
        else:
            print("case is not working")
        token_1 = post_1.json()['data']['token']
        register_headers_2 = \
            {
                'Authorization': f'Bearer {token_1}',
                'Content-Type': 'application/json;charset=UTF-8',
                'Accept': 'application/json, text/plain, /'
            }
        print("Узнаем аккаунт пользователя")
        get_1 = requests.get(url=url_1+url_acc, headers=register_headers_2)
        assert 200 == post_1.status_code
        if get_1.status_code == 200:
            get_1 = get_1.json()
        account_main = None
        for account in get_1['data']:
            if account['name'] == "Основной счет USD":
                account_main = account['id']  # account_ustd_main  это переменная которую система использует как номер счета
                break
        print("Аккаунт для пополнения основного счета = id ", account_main)
        print("--------------------------")
        print("Теперь админом кидаем деньги на основной счет пользователю")
        print("Авторизация админом")

        auf_hed_admin = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, /'
        }
        body_admin = {

            "login": admin_login,
            "password": admin_password
        }
        post_admin = requests.post(url=url_1+url_auf, headers=auf_hed_admin, json=body_admin)
        print(post_admin.status_code)
        assert 200 == post_admin.status_code
        if post_admin.status_code == 200:
            print("Токен админа получил.")
        else:
            print("чтото посло не так")
        token_admin = post_admin.json()['data']['token']
        register_admin = \
            {
                'Authorization': f'Bearer {token_admin}',
                'Content-Type': 'application/json;charset=UTF-8',
                'Accept': 'application/json, text/plain, /'
            }
        post_body = {
            "credit_account_id": "3",
            "debit_account_id": account_main,
            "amount": "50000"
        }
        post_money = requests.post(url=url_1+url_money, headers=register_admin, json=post_body)
        print(post_money.json())

        if post_money.status_code == 202:
            print("Статус код", post_money.status_code)
            print("Баблишко на счету")
            print("----------")
        else:
            print(post_money.json())
            print(post_money.status_code, "чет натупилось")


# Использование класса UserGenerator для создания 10 пользователей
generator = UserGenerator()
generator.generate_users(20)
