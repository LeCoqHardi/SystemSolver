from sympy import *
import os
import platform

# Resolver est un script python permettant de résoudre des équations 
# Créé par LeCoqHardi, disponible sur Github.
# https://www.twitch.tv/lecoqhardi // https://www.twitter.com/LeCoqHardi__ 

# This part is used to detect the OS you use and clear the console.
OperatingSystem = platform.system() 

if OperatingSystem == "Windows":
        os.system('cls')
else:
        os.system('clear')
#-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

print("======================[Resolver]======================")
print("Pour résoudre des équations, il faut savoir comment s'écrivent les équations.")
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


x = Symbol('x')
y = Symbol('y')
z = Symbol('z')


print("Entrez votre équation :")
equa = input()
print("Pour résoudre l'équation, il faut changer l'inconnu par la valeur/les valeurs :")
print(solve(equa))
