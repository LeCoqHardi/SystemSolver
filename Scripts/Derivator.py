# Derivator is a python script used to derivate functions.
# Made by LeCoqHardi, available on Github.
# https://www.twitch.tv/lecoqhardi // https://www.twitter.com/LeCoqHardi__ // https://www.github.com/lecoqhardi

from sympy import *
import os
import platform
import sys

# This part is used to detect the OS you use and clear the console.
OperatingSystem = platform.system()

if OperatingSystem == "Windows":
    os.system("cls")
else:
    os.system("clear")

# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

print("\033[1;31;40m===============================================================")
print("______          _            _                         ")
print("|  _  \        (_)          | |                        ")
print("| | | |___ _ __ ___   ____ _| |_ ___  _ __ _ __  _   _ ")
print("| | | / _ \ '__| \ \ / / _` | __/ _ \| '__| '_ \| | | |")
print("| |/ /  __/ |  | |\ V / (_| | || (_) | |_ | |_) | |_| |")
print("|___/ \___|_|  |_| \_/ \__,_|\__\___/|_(_)| .__/ \__, |")
print("                                          | |     __/ |")
print("                                          |_|    |___/ ")
print("===============================================================")
print("\033[1;37;40m\n")
print("To derivate an equation in Python, you have to know how to write them.")
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

# Set up  sympy
x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/


# Derivative part
f = input("Type your equation : ")
print("Before Derivation : ")
print("\033[1;32;40m", f, "\033[1;37;40m")
f_prime = diff(f, x)
print("After Derivation : ")
print("\033[1;32;40m", f_prime, "\033[1;37;40m")

# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

leave = 0
while (leave != 1 or leave !=2):
    print("")
    print("Do you want to continue using Maths-Useful.py, or quit ? [1 - Continue // 2 - Quit] ")
    leave = int(input("Answer > "))
    if leave == 1:
        os.system("python3 Launcher.py")
    elif leave == 2:
        sys.exit()
