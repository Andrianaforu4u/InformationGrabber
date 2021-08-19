from colorama import Fore, Back, Style

f = open('helloworld.txt','r')
message = f.read()

print(Back.GREEN + message)


