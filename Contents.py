from colorama import Fore, Back, Style


f = open('Creds.txt','r')
message = f.read()

def Contents():
  print(Fore.GREEN + message)


