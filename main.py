import requests
import os.path
import time
from datetime import datetime

#----------------------------------Вход----------------------------------
def tokenlogin(login, password):
 headers = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
 }


 json_data = {
    'login': login,
    'password': password,
    'undelete': False,
    'login_source': None,
    'gift_code_sku_id': None,
 }

 r = requests.post('https://discord.com/api/v9/auth/login', headers=headers, json=json_data)
 return r.json()['token']

while not(os.path.exists('tokenlogin.txt')):
 login = input("\033[01;38;05;136m Тел или почта: \033[0m	")
 password = input("\033[01;38;05;136m Пароль: \033[0m	")

 with open('tokenlogin.txt', 'w') as f:
    f.write(f'не делитесь этим документом иначе вас могут взломать!!!\n{tokenlogin(login, password)}')

with open('tokenlogin.txt', 'r') as f:
  authorization = f.readlines()[1]

#----------------------------------Рабоота----------------------------------
headers = {
    'authorization': authorization,
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

while True:
 def date():
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        day, month, year = time.strftime("%d.%m.%Y", time.localtime()).split('.')
        return f'{day} {months[int(month) - 1]} {time.strftime("%H:%M", time.localtime())}'
 def timedelta():
     timedelta = datetime(day=1, month=6, year=datetime.now().year) - datetime.now()
     days = str(timedelta).split(':')[0].split('days')[0].replace(" ", "")
     hour = str(timedelta).split(':')[0].split('days')[1].replace(", ", "")
     minutes = str(timedelta).split(':')[1]
     return f'До Лета осталось дней: {days}, часов: {hour}, минут: {minutes}'

 json_data = {
    'bio': f'13 лет\nТюмень\nАндрей\nВремя: {date()}\n{timedelta()}',
 }
 requests.patch('https://discord.com/api/v9/users/%40me/profile', headers=headers, json=json_data)
 print(date())
 print(timedelta())
 time.sleep(60)
