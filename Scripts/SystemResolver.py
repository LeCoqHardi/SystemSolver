
# SystemResolver is a Python script used to resolve systems with 2 or 3 equations
# Made by LeCoqHardi, available on Github
# https://www.twitch.tv/lecoqhardi // https://www.twitter.com/LeCoqHardi__ // https://Github.com/lecoqhardi

import numpy as np  # Import "numpy"
import os
import platform
import sys

OperatingSystem = platform.system()

if OperatingSystem == "Windows":
    os.system("cls")
else:
    os.system("clear")

print("\033[1;31;40m=====================================================================================")
print(" _____           _                ______                _                            ")
print("/  ___|         | |               | ___ \              | |                           ")
print("\ `--. _   _ ___| |_ ___ _ __ ___ | |_/ /___  ___  ___ | |_   _____ _ __ _ __  _   _ ")
print(" `--. \ | | / __| __/ _ \ '_ ` _ \|    // _ \/ __|/ _ \| \ \ / / _ \ '__| '_ \| | | |")
print("/\__/ / |_| \__ \ ||  __/ | | | | | |\ \  __/\__ \ (_) | |\ V /  __/ |_ | |_) | |_| |")
print("\____/ \__, |___/\__\___|_| |_| |_\_| \_\___||___/\___/|_| \_/ \___|_(_)| .__/ \__, |")
print("        __/ |                                                           | |     __/ |")
print("       |___/                                                            |_|    |___/ ")
print("=====================================================================================")
print("\033[1;37;40m ")

nbEqua = int(input("How much equations do your system contain ? "))  # Number of equations

# -----------------------------------------------Super-Partie des équations à 2 inconnues---------------------------------------------------------

if (
    nbEqua == 2
):  # Dois-je réellement expliquer la fonction if ? Bah en gros ça test votre réponse, et si elle est égale à celle dans sa condition vous rentrez dans sa boucle

    # -------------------------------------------------Sous-Partie de la première équation------------------------------------------------------------
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[FIRST EQUATION] \033[1;37;40m Type the number of the first variable \033[1;37;40m of the \033[1;32;40mfirst equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val1 = int(
        input()
    )  # Variable contenant la valeur de la première inconnue de la première équation
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[FIRST EQUATION] \033[1;37;40m Type the number of the second variable \033[1;37;40m of \033[1;32;40mthe first equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val2 = int(
        input()
    )  # Variable contenant la valeur de la dexième inconnue de la première équation

    # -------------------------------------------------Sous-Partie de la deuxième équation------------------------------------------------------------

    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[SECOND EQUATION] \033[1;37;40m Type the number of the first variable \033[1;37;40m of \033[1;32;40mthe second equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val3 = int(
        input()
    )  # Variable contenant la valeur de la première inconnue de la deuxième équation
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[SECOND EQUATION] \033[1;37;40m Type the number of the second variable \033[1;37;40m of \033[1;32;40mthe second equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val4 = int(
        input()
    )  # Variable contenant la valeur de la dexième inconnue de la deuxième équation

    # -------------------------------------------------Sous-Partie des résultats----------------------------------------------------------------------

    print("-----------------------------------------------")  # Encore un print
    print("\033[1;32;40m[RESULT 1] \033[1;37;40m Type the result of \033[1;32;40mthe first \033[1;37;40m equation")  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    res1 = int(input())  # Variable contenant le résultat de la première équation
    print("-----------------------------------------------")  # Encore un print
    print("\033[1;32;40m[RESULT 2] \033[1;37;40m Type the result of \033[1;32;40mthe second \033[1;37;40m equation")  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    res2 = int(input())  # Variable contenant le résultat de la deuxième équation
    a = np.array(
        [[val1, val2], [val3, val4]]
    )  # Commande compliquée de la bibliothèque "numpy"
    b = np.array([res1, res2])  # Commande compliquée de la bibliothèque "numpy"
    x = np.linalg.solve(a, b)  # Commande compliquée de la bibliothèque "numpy"
    print("=============================================")  # Encore un print
    print(
        "Your variables or equals to : \033[1;32;40m", x, "\033[1;37;40m"
    )  # Encore un print mais lui il affiche les résultats de vos inconnues
    print("=============================================")  # Encore un print


# -----------------------------------------------Super-Partie des équations à 3 inconnues----------------------------------------------------------

if nbEqua == 3:
    # -----------------------------------------------Sous-Partie de la première équation---------------------------------------------------------------

    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[FIRST EQUATION] \033[1;37;40m Type the number of the first variable \033[1;37;40m of \033[1;32;40mthe first equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val1 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[FIRST EQUATION] \033[1;37;40m Type the number of the second variable \033[1;37;40m of \033[1;32;40mthe first equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val2 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[FIRST EQUATION] \033[1;37;40m Type the number of the third variable \033[1;37;40m of \033[1;32;40mthe first equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val3 = int(input())  # voir au dessus

    # -----------------------------------------------Sous-Partie de la deuxième équation----------------------------------------------------------------

    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[SECOND EQUATION] \033[1;37;40m Type the number of the first variable \033[1;37;40m of \033[1;32;40mthe second equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val4 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[SECOND EQUATION] \033[1;37;40m Type the number of the second variable \033[1;37;40m of \033[1;32;40mthe second equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val5 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[SECOND EQUATION] \033[1;37;40m Type the number of the third variable \033[1;37;40m of \033[1;32;40mthe second equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val6 = int(input())  # voir au dessus

    # -----------------------------------------------Sous-Partie de la troisième équation---------------------------------------------------------------

    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[THIRD EQUATION] \033[1;37;40m Type the number of the first variable \033[1;37;40m of \033[1;32;40mthe third equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val7 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[THIRD EQUATION] \033[1;37;40m Type the number of the second variable \033[1;37;40m of \033[1;32;40mthe third equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val8 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[THIRD EQUATION] \033[1;37;40m Type the number of the third variable \033[1;37;40m of \033[1;32;40mthe third equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val9 = int(input())  # voir au dessus

    # ------------------------------------------------Sous-Partie des résultats--------------------------------------------------------------------------

    print("-----------------------------------------------")  # Encore un print
    print("\033[1;32;40m[RESULT 1] \033[1;37;40m Type the result of \033[1;32;40mthe first \033[1;37;40m equation")  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    res1 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print("\033[1;32;40m[RESULT 2] \033[1;37;40m Type the result of \033[1;32;40mthe second \033[1;37;40m equation")  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    res2 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print("\033[1;32;40m[RESULT 3] \033[1;37;40m Type the result of \033[1;32;40mthe third \033[1;37;40m equation")  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    res3 = int(input())  # voir au dessus
    a = np.array([[val1, val2, val3], [val4, val5, val6], [val7, val8, val9]])  # voir au dessus
    b = np.array([res1, res2, res3])  # voir au dessus
    x = np.linalg.solve(a, b)  # voir au dessus
    print("=============================================")  # Encore un print
    print("Your variables or equals to : \033[1;32;40m", x, "\033[1;37;40m")  # Encore un print mais lui il affiche les résultats de vos inconnues
    print("=============================================")  # Encore un print
if nbEqua == 4:
    # -----------------------------------------------Sous-Partie de la première équation---------------------------------------------------------------

    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[FIRST EQUATION] \033[1;37;40m Type the number of the first variable \033[1;37;40m of \033[1;32;40mthe first equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val1 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[FIRST EQUATION] \033[1;37;40m Type the number of the second variable \033[1;37;40m of \033[1;32;40mthe first equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val2 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[FIRST EQUATION] \033[1;37;40m Type the number of the third variable \033[1;37;40m of \033[1;32;40mthe first equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val3 = int(input())  # voir au dessus
    print(
        "\033[1;32;40m[FIRST EQUATION] \033[1;37;40m Type the number of the fourth variable \033[1;37;40m of \033[1;32;40mthe first equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val4 = int(input())  # voir au dessus

    # -----------------------------------------------Sous-Partie de la deuxième équation----------------------------------------------------------------

    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[SECOND EQUATION] \033[1;37;40m Type the number of the first variable \033[1;37;40m of \033[1;32;40mthe second equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val5 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[SECOND EQUATION] \033[1;37;40m Type the number of the second variable \033[1;37;40m of \033[1;32;40mthe second equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val6 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[SECOND EQUATION] \033[1;37;40m Type the number of the third variable \033[1;37;40m of \033[1;32;40mthe second equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val7 = int(input())  # voir au dessus
    print(
        "\033[1;32;40m[SECOND EQUATION] \033[1;37;40m Type the number of the fourth variable \033[1;37;40m of \033[1;32;40mthe second equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val8 = int(input())  # voir au dessus

    # -----------------------------------------------Sous-Partie de la troisième équation---------------------------------------------------------------

    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[THIRD EQUATION] \033[1;37;40m Type the number of the first variable \033[1;37;40m of \033[1;32;40mthe third equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val9 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[THIRD EQUATION] \033[1;37;40m Type the number of the second variable \033[1;37;40m of \033[1;32;40mthe third equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val10 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[THIRD EQUATION] \033[1;37;40m Type the number of the third variable \033[1;37;40m of \033[1;32;40mthe third equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val11 = int(input())  # voir au dessus
    print(
        "\033[1;32;40m[THIRD EQUATION] \033[1;37;40m Type the number of the fourth variable \033[1;37;40m of \033[1;32;40mthe third equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val12 = int(input())  # voir au dessus

    # -----------------------------------------------Sous-Partie de la quatrième équation---------------------------------------------------------------

    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[FOURTH EQUATION] \033[1;37;40m Type the number of the first variable \033[1;37;40m of \033[1;32;40mthe fourth equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val13 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[FOURTH EQUATION] \033[1;37;40m Type the number of the second variable \033[1;37;40m of \033[1;32;40mthe fourth equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val14 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print(
        "\033[1;32;40m[FOURTH EQUATION] \033[1;37;40m Type the number of the third variable \033[1;37;40m of \033[1;32;40mthe fourth equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val15 = int(input())  # voir au dessus
    print(
        "\033[1;32;40m[FOURTH EQUATION] \033[1;37;40m Type the number of the fourth variable \033[1;37;40m of \033[1;32;40mthe fourth equation \033[1;37;40m (without the letter)"
    )  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    val16 = int(input())  # voir au dessus

    # ------------------------------------------------Sous-Partie des résultats--------------------------------------------------------------------------

    print("-----------------------------------------------")  # Encore un print
    print("\033[1;32;40m[RESULT 1] \033[1;37;40m Type the result of the first \033[1;37;40m equation")  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    res1 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print("\033[1;32;40m[RESULT 2] \033[1;37;40m Type the result of the second \033[1;37;40m equation")  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    res2 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print("\033[1;32;40m[RESULT 3] \033[1;37;40m Type the result of the third \033[1;37;40mequation")  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    res3 = int(input())  # voir au dessus
    print("-----------------------------------------------")  # Encore un print
    print("\033[1;32;40m[RESULT 4] \033[1;37;40m Type the result of the fourth \033[1;37;40mequation")  # Encore un print
    print("-----------------------------------------------")  # Encore un print
    res4 = int(input())  # voir au dessus
    a = np.array(
        [
            [val1, val2, val3, val4],
            [val5, val6, val7, val8],
            [val9, val10, val11, val12],
            [val13, val14, val15, val16],
        ]
    )  # voir au dessus
    b = np.array([res1, res2, res3, res4])  # voir au dessus
    x = np.linalg.solve(a, b)  # voir au dessus
    print("=============================================")  # Encore un print
    print(
        "Your variables or equals to : \033[1;32;40m", x, "\033[1;37;40m"
    )  # Encore un print mais lui il affiche les résultats de vos inconnues
    print("=============================================")  # Encore un print
if nbEqua > 4:
    print("Wrong entry.")


leave = 0
while (leave != 1 or leave !=2):
    print("\033[1;37;40m")
    print("Do you want to continue using Maths-Useful.py, or quit ? [1 - Continue // 2 - Quit] ")
    leave = int(input("Answer > "))
    if leave == 1:
        os.system("python3 Launcher.py")
    elif leave == 2:
        sys.exit()

