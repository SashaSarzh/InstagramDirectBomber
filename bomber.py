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

author: @SashaSarzh
instagram: @jidkiypuk2\n """ + Style.RESET_ALL)

webbrowser.open('https://instagram.com/jidkiypuk2')

nostop = 0

accounts = input("Input here list of your account(If haven't type Enter): ")

if not accounts:
    username = input("Your Login: ")
    password = input("Your Password: ")
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

user = input("Victims nickname: ")

url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+user+"&rank_token=0.3953592318270893&count=1"
response = requests.get(url)
respJSON = response.json()
user_id = str( respJSON['users'][0].get("user").get("pk") )

while True:
    if user == "niggvard" or user == "jidkiypuk2":
        print("No no no")
        sys.exit()
    else: break

message = input("Text of message: ")

if istimes == 0:
    times = int(input("How many messages you want send: "))
elif istimes == 1:
    times = NumberOfLine

print("You will use bomber ", times,"times ", user_id, "with message: ", message, ".")
ask = input("Do you want continue[y/n]:")

if ask == 'y':
	print('Starting..')
elif ask == 'n':
	print('Stopping..')
	sys.exit()
else:
	print('Stopping')
	sys.exit()


while times > nostop:
    nostop = nostop + 1
    api.sendMessage(user_id,message)
    print(nostop, ">> Send", user, ": ", message)



