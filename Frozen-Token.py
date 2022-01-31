
#Copyright Maf1ozos#6666
#Skid This = Clown
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Frozen loading")
print(f"{Fore.WHITE}")
progressbar = tqdm([2,4,6,8,9,10])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Looking For Updates: ')
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Frozen loading")
print(f"{Fore.GREEN}")
progressbar = tqdm([2,4,6,8,9,10,11,12,13,14,15])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Looking For Errors: ')
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Loading Frozen:")
print(f"{Fore.RED}")
progressbar = tqdm([1,2,3])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading Hud: ')
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Frozen Loaded!")
print(f"{Fore.WHITE}")
progressbar = tqdm([1,2,])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Checking For Something: ')
import os
os.system('CLS')  
os.system("title Frozen Token Generator")


print("                                                                                                       ")
print("  █████▒██▀███   ▒█████  ▒███████▒▓  █████     ███  █    ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █    ")
print("   ▓██   ▒▓██ ▒ ██▒▒██▒  ██▒▒ ▒ ▒ ▄▀░▓█   ▀  ██ █   █    ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █    ")
print("  ▒████ ░▓██ ░▄█ ▒▒██░  ██▒░ ▒ ▄▀▒░ ▒███   ▓██  ▀█ ██▒   ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒   ")
print("  ░▓█▒  ░▒██▀▀█▄  ▒██   ██░  ▄▀▒   ░▒▓█  ▄ ▓██▒  ▐▌██▒   ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ")
print("  ░▒█░   ░██▓ ▒██▒░ ████▓▒░▒███████▒░▒████▒▒██░   ▓██░     ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░   ")
print("  ▒ ░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒░   ▒ ▒      ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒     ")
print("   ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒ ▒ ░ ▒ ░ ░  ░░ ░░   ░ ▒░       ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░   ")
print("  ░ ░     ░░   ░ ░ ░ ░ ▒  ░ ░ ░ ░ ░   ░      ░   ░ ░      ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░     ") 
print("     ░         ░ ░    ░ ░       ░  ░         ░                 ░ ░  ░  ░      ░  ░         ░           ")
print("                                                                                                       ")
print("                           > Made by Maf1ozos#6666 X Dm Me if someone skidded this                                                                                              ")


import random
while True:
	char1  = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890.-_"
	char2 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890"

	num1 = int(input("Input How Much Tokens:"))
	num2 = int(input("How much Token characters(default is 59):"))
	Choice1 = str(input("y/n:"))




	if Choice1 == 'y':
		for p in range(num1):
			password = ""
			for c in range(num2):
				password += random.choice(char1)
			print(password)
	if Choice1 == 'n':
		for p in range(num1):
			password = ""
			for c in range(num2):
				password += random.choice(char2)
			print(password)
