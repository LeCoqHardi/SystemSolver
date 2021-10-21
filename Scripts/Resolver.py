from sympy import *
import os
import platform
import sys

# Resolver est un script python permettant de résoudre des équations
# Créé par LeCoqHardi, disponible sur Github.
# https://www.twitch.tv/lecoqhardi // https://www.twitter.com/LeCoqHardi__

# This part is used to detect the OS you use and clear the console.
OperatingSystem = platform.system()

if OperatingSystem == "Windows":
    os.system("cls")
else:
    os.system("clear")
# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/


print("\033[1;31;40m===============================================================")
print("______                _                            ")
print("| ___ \              | |                           ")
print("| |_/ /___  ___  ___ | |_   _____ _ __ _ __  _   _ ")
print("|    // _ \/ __|/ _ \| \ \ / / _ \ '__| '_ \| | | |")
print("| |\ \  __/\__ \ (_) | |\ V /  __/ |_ | |_) | |_| |")
print("\_| \_\___||___/\___/|_| \_/ \___|_(_)| .__/ \__, |")
print("                                      | |     __/ |")
print("                                      |_|    |___/ ")
print("===============================================================")
print("\033[1;37;40m\n")
print("To Solve an equation in Python, you have to know how to write them.")
print("---------------------------------")
print("That's how :")
print("2x -> 2*x")
print("x^n -> x**n")
print("cos(x) -> cos(x)")
print("sin(x) -> sin(x)")
print("ln(x) -> ln(x)")
print("e^x -> exp(x)")
print("---------------------------------")
print("Variables are : x, y and z.")


x = Symbol("x")
y = Symbol("y")
z = Symbol("z")


print("Type your equation :")
equa = input()
print("To resolve the equation, you have to change the variables by this/those numbers :")
print("\033[1;32;40m", solve(equa),"\033[1;37;40m")



leave = 0
while (leave != 1 or leave !=2):
    print("")
    print("Do you want to continue using Maths-Useful.py, or quit ? [1 - Continue // 2 - Quit] ")
    leave = int(input("Answer > "))
    if leave == 1:
        os.system("python3 Launcher.py")
    elif leave == 2:
        sys.exit()

