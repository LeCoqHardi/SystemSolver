from sympy import *
import os
import platform
import sys


# Syracuse.py is a python script is a python script used to try a number given by the user to the collatz conjecture
# Made by LeCoqHardi, available on Github

# https://www.twitch.tv/lecoqhardi // https://www.twitter.com/LeCoqHardi__ // https://www.github.com/lecoqhardi


# This part clear the screen
OperatingSystem = platform.system()

if OperatingSystem == "Windows":
    os.system("cls")
else:
    os.system("clear")

# Shows banner
print("\033[1;31;40m===============================================================\n")
print(" _____                                                   ")
print("/  ___|                                                  ")
print("\ `--. _   _ _ __ __ _  ___ _   _ ___  ___   _ __  _   _ ")
print(" `--. \ | | | '__/ _` |/ __| | | / __|/ _ \ | '_ \| | | |")
print("/\__/ / |_| | | | (_| | (__| |_| \__ \  __/_| |_) | |_| |")
print("\____/ \__, |_|  \__,_|\___|\__,_|___/\___(_) .__/ \__, |")
print("        __/ |                               | |     __/ |")
print("       |___/                                |_|    |___/ ")
print("===============================================================")
print("\033[1;37;40m\n")
# ask to user
nbEntre = int(input("Type the number you want to try : "))
nbTest = nbEntre
nbTours = 0
nbToursOdd = 0
nbToursEven = 0
print("You want to try the number", "\033[1;32;40m", nbEntre, "\033[1;37;40m :")


while nbTest != 1: # while the number entered by the user is different to 1
    if (nbTest % 2) == 0: # if it's even
        nbTest = nbTest / 2 # divide by 2
        nbToursEven = nbToursEven + 1
    else: #if it's odd
        nbTest = nbTest * 3 + 1 # Times 3 + 1
        nbToursOdd = nbToursOdd + 1

    nbTours = nbTours + 1 # adds one to loops

# This part shows the result
print("For the number ", "\033[1;32;40m", nbEntre, "\033[1;37;40m  there was ", "\033[1;36;40m", nbTours, "\033[1;37;40m  loops before getting 1, with : ","\033[1;33;40m", nbToursOdd, "\033[1;37;40m odd loops and ","\033[1;33;40m", nbToursEven, " \033[1;37;40meven loops."  ) # shows number entered and loops turns

# This part asks if you want to stay or leave
leave = 0
while (leave != 1 or leave !=2):
    print("")
    print("Do you want to continue using Maths-Useful.py, or quit ? [1 - Continue // 2 - Quit] ")
    leave = int(input("Answer > "))
    if leave == 1:
        os.system("python3 Launcher.py")
    elif leave == 2:
        sys.exit()