# Launcher.py is the main script, use it to choose between all little scripts. (you can still use littles scripts alone)
# Made by LeCoqHardi, available on Github
# Free to use
# https://www.twitch.tv/lecoqhardi // https://www.twitter.com/LeCoqHardi__ // https://www.github.com/lecoqhardi
# All the imports are importants, don't forget to install python library with pip
import os
import platform
import sys

# This part is used to detect the OS you use and clear the console.
OperatingSystem = platform.system()

if OperatingSystem == "Windows":
    os.system("cls")
else:
    os.system("clear")

print("\033[1;31;40m=====================================================================================")
print("___  ___      _   _                _   _           __       _               ")
print("|  \/  |     | | | |              | | | |         / _|     | |              ")
print("| .  . | __ _| |_| |__  ___ ______| | | |___  ___| |_ _   _| |  _ __  _   _ ")
print("| |\/| |/ _` | __| '_ \/ __|______| | | / __|/ _ \  _| | | | | | '_ \| | | |")
print("| |  | | (_| | |_| | | \__ \      | |_| \__ \  __/ | | |_| | |_| |_) | |_| |")
print("\_|  |_/\__,_|\__|_| |_|___/       \___/|___/\___|_|  \__,_|_(_) .__/ \__, |")
print("                                                               | |     __/ |")
print("                                                               |_|    |___/ ")
print("=====================================================================================")
print("\033[1;37;40m\n")

print("What do you want to do ?")
print("==========================================")
print("")
print("1 - Derive a function")
print("")
print("2 - Resolve an equation")
print("")
print("3 - Solve a System")
print("")
print("4 - Try a number to the Collatz Conjecture")
print("")
print("0 - Exit")
print("==========================================")
answer = int(input("Answer > "))

if answer == 1:
    os.system("python3 ./Scripts/Derivator.py")
elif answer == 2:
    os.system("python3 ./Scripts/Resolver.py")
elif answer == 3:
    os.system("python3 ./Scripts/SystemResolver.py")
elif answer == 4:
    os.system("python3 ./Scripts/Syracuse.py")
elif answer == "0":
    sys.exit()
