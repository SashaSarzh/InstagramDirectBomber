from InstagramAPI import InstagramAPI
from colorama import Fore, Back, Style
import sys
import webbrowser
import time
import requests
import json


print(Fore.GREEN + """ 

░░███╗░░███╗░░██╗░██████╗████████╗░░██╗██╗██████╗░░█████╗░███╗░░░███╗██████╗░██████╗░██████╗░
░████║░░████╗░██║██╔════╝╚══██╔══╝░██╔╝██║██╔══██╗██╔══██╗████╗░████║██╔══██╗╚════██╗██╔══██╗
██╔██║░░██╔██╗██║╚█████╗░░░░██║░░░██╔╝░██║██████╦╝██║░░██║██╔████╔██║██████╦╝░█████╔╝██████╔╝
╚═╝██║░░██║╚████║░╚═══██╗░░░██║░░░███████║██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗░╚═══██╗██╔══██╗
███████╗██║░╚███║██████╔╝░░░██║░░░╚════██║██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝██████╔╝██║░░██║
╚══════╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░░░░░░╚═╝╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝

author: idontknowwhatiwilldo
instagram: @jidkiypuk2\n """ + Style.RESET_ALL)

webbrowser.open('https://instagram.com/jidkiypuk2')

nostop = 0

accounts = input("Впиши сюда название своего текстового файла с аккаунтом(если нет, нажми Enter чтобы продолжить): ")

if not accounts:
    username = input("Твой Логин: ")
    password = input("Твой Пароль: ")
    api = InstagramAPI(username, password)
    api.login()
    istimes = 0
else:
    f = open(accounts, 'r')
    NumberOfLine = 0
    for line in f:
        NumberOfLine += 1
    username, password = line.split(':')
    print ("Логин найден: ", username)
    print ("Пароль найден: ********")
    api = InstagramAPI(username, password)
    api.login()
    istimes = 0

user = input("Ник жертвы: ")

url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+user+"&rank_token=0.3953592318270893&count=1"
response = requests.get(url)
respJSON = response.json()
user_id = str( respJSON['users'][0].get("user").get("pk") )

message = input("Сообщение которое вы хотите отправить: ")

if istimes == 0:
    times = int(input("Сколько сообщений вы хотите отправить: "))
elif istimes == 1:
    times = NumberOfLine

print("Вы хотите отправить бомбер ", times,"раз(а) ", user_id, "сообщением: ", message, ".")
ask = input("Вы уверены что хотите  продолжить[y/n]:")

if ask == 'y':
	print('Начинаю')
elif ask == 'n':
	print('Останавливаю скрипт')
	sys.exit()
else:
	print('Останавливаю скрипт')
	sys.exit()


while times > nostop:
    nostop = nostop + 1
    api.sendMessage(user_id,message)
    print(nostop, ">> Отправлено", user, ": ", message)



