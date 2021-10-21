from sympy import *
import os
import platform


# [FR]
# Syracuse.py est un script python permettant de tester la suite de Syracuse entre deux nombres donnés par l'utilisateur
# Créé par LeCoqHardi, disponible sur Github.

# [EN]
# Syracuse.py is a python script is a python script used to try a number given by the user to the collatz conjecture
# Made by LeCoqHardi, available on Github

# https://www.twitch.tv/lecoqhardi // https://www.twitter.com/LeCoqHardi__ // https://www.github.com/lecoqhardi


# This part clear the screen
OperatingSystem = platform.system()

if OperatingSystem == "Windows":
    os.system("cls")
else:
    os.system("clear")


print("===============================================================")
print(" _____                                                   ")
print("/  ___|                                                  ")
print("\ `--. _   _ _ __ __ _  ___ _   _ ___  ___   _ __  _   _ ")
print(" `--. \ | | | '__/ _` |/ __| | | / __|/ _ \ | '_ \| | | |")
print("/\__/ / |_| | | | (_| | (__| |_| \__ \  __/_| |_) | |_| |")
print("\____/ \__, |_|  \__,_|\___|\__,_|___/\___(_) .__/ \__, |")
print("        __/ |                               | |     __/ |")
print("       |___/                                |_|    |___/ ")
print("===============================================================")
print("")
nbEntre = int(input("Type the number you want to try : "))
nbTest = nbEntre
nbTours = 0
print("You want to try the number ", nbEntre, " :")

while nbTest != 1 or nbTours > 50000:
    if (nbTest % 2) == 0:
        nbTest = nbTest / 2
    else:
        nbTest = nbTest * 3 + 1

    nbTours = nbTours + 1


print("For the number ", nbEntre, " there was ", nbTours, " loops before getting 1")
