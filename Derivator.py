# Derivator est un script python permettant de dériver automatiquement une fonction.
# Créé par LeCoqHardi, disponible sur Github.
# https://www.twitch.tv/lecoqhardi // https://www.twitter.com/LeCoqHardi__

from sympy import *
import os
import platform

# This part is used to detect the OS you use and clear the console.
OperatingSystem = platform.system()

if OperatingSystem == "Windows":
    os.system("cls")
else:
    os.system("clear")

# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

print("===============================================================")
print("______          _            _                         ")
print("|  _  \        (_)          | |                        ")
print("| | | |___ _ __ ___   ____ _| |_ ___  _ __ _ __  _   _ ")
print("| | | / _ \ '__| \ \ / / _` | __/ _ \| '__| '_ \| | | |")
print("| |/ /  __/ |  | |\ V / (_| | || (_) | |_ | |_) | |_| |")
print("|___/ \___|_|  |_| \_/ \__,_|\__\___/|_(_)| .__/ \__, |")
print("                                          | |     __/ |")
print("                                          |_|    |___/ ")
print("===============================================================")
print("")
print("Pour dériver en python, il faut savoir comment s'écrivent les équations.")
print("---------------------------------")
print("Voilà comment elles s'écrivent :")
print("2x -> 2*x")
print("x^n -> x**n")
print("cos(x) -> cos(x)")
print("sin(x) -> sin(x)")
print("ln(x) -> ln(x)")
print("e^x -> exp(x)")
print("---------------------------------")
print("Les inconnues à utiliser sont x, y et z.")

# Partie préparation de sympy
x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/


# Partie dérivation
print("Entrez votre équation :")
f = input()
print("Avant la dérivation : ")
print(f)
f_prime = diff(f, x)
print("Après la dérivation : ")
print(f_prime)

# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
