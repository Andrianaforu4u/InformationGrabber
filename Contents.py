from colorama import Fore, Back, Style

f = open('Creds.txt','r')
message = f.read()

print(Back.GREEN + message)


