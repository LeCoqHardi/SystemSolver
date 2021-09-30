# SystemResolver est un script Python permettant de résoudre des systèmes à 2 ou 3 équations (et surement plus dans le futur)
# Créé par LeCoqHardi, disponible sur Github.
# https://www.twitch.tv/lecoqhardi // https://www.twitter.com/LeCoqHardi__ 

import numpy as np # Importation de la bilbiothèque "numpy"
import os
import platform

OperatingSystem = platform.system()

if OperatingSystem == "Windows":
        os.system('cls')
else:
        os.system('clear')



print("================[SystemResolver]================") # Bon en gros les print ça affiche voilà 
print("Combien votre système contient-il d'équations ?") # Encore un print 
nbEqua = int(input()) # Variable du nombre d'équations du système

#-----------------------------------------------Super-Partie des équations à 2 inconnues---------------------------------------------------------

if nbEqua == 2: # Dois-je réellement expliquer la fonction if ? Bah en gros ça test votre réponse, et si elle est égale à celle dans sa condition vous rentrez dans sa boucle

#-------------------------------------------------Sous-Partie de la première équation------------------------------------------------------------
        print("-----------------------------------------------") # Encore un print
        print ("[1ERE EQUATION] Entrez la valeur de la première inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val1 = int(input()) # Variable contenant la valeur de la première inconnue de la première équation
        print("-----------------------------------------------") # Encore un print
        print ("[1ERE EQUATION] Entrez la valeur de la deuxième inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val2 = int(input()) # Variable contenant la valeur de la dexième inconnue de la première équation        

#-------------------------------------------------Sous-Partie de la deuxième équation------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("[2EME EQUATION] Entrez la valeur de la première inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val3 = int(input()) # Variable contenant la valeur de la première inconnue de la deuxième équation
        print("-----------------------------------------------") # Encore un print
        print ("[2EME EQUATION] Entrez la valeur de la deuxième inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val4 = int(input()) # Variable contenant la valeur de la dexième inconnue de la deuxième équation

#-------------------------------------------------Sous-Partie des résultats----------------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("[RESULTAT 1] Entrez le résultat de la première équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res1 = int(input()) # Variable contenant le résultat de la première équation
        print("-----------------------------------------------") # Encore un print
        print ("[RESULTAT 2] Entrez le résultat de la deuxième équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res2 = int(input()) # Variable contenant le résultat de la deuxième équation
        a = np.array([[val1,val2], [val3,val4]]) # Commande compliquée de la bibliothèque "numpy" 
        b = np.array([res1,res2]) # Commande compliquée de la bibliothèque "numpy"
        x = np.linalg.solve(a, b) # Commande compliquée de la bibliothèque "numpy"
        print("=============================================") # Encore un print
        print("Vos inconnues sont respectivement égales à", x) # Encore un print mais lui il affiche les résultats de vos inconnues
        print("=============================================") # Encore un print
        

#-----------------------------------------------Super-Partie des équations à 3 inconnues----------------------------------------------------------  
     
if nbEqua == 3:
#-----------------------------------------------Sous-Partie de la première équation---------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("[1ERE EQUATION] Entrez la valeur de la première inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val1 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[1ERE EQUATION] Entrez la valeur de la deuxième inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val2 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[1ERE EQUATION] Entrez la valeur de la troisième inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val3 = int(input()) # voir au dessus

#-----------------------------------------------Sous-Partie de la deuxième équation----------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("[2EME EQUATION] Entrez la valeur de la première inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val4 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[2EME EQUATION] Entrez la valeur de la deuxième inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val5 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[2EME EQUATION] Entrez la valeur de la troisième inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val6 = int(input()) # voir au dessus

#-----------------------------------------------Sous-Partie de la troisième équation---------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("[3EME EQUATION] Entrez la valeur de la première inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val7 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[3EME EQUATION] Entrez la valeur de la deuxième inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val8 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[3EME EQUATION] Entrez la valeur de la troisième inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val9 = int(input()) # voir au dessus

#------------------------------------------------Sous-Partie des résultats-------------------------------------------------------------------------- 

        print("-----------------------------------------------") # Encore un print
        print ("[RESULTAT 1] Entrez le résultat de la première équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res1 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[RESULTAT 2] Entrez le résultat de la deuxième équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res2 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print("[RESULTAT 3] Entrez le résultat de la troisième équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res3 = int(input()) # voir au dessus
        a = np.array([[val1,val2,val3], [val4,val5,val6], [val7,val8,val9]]) # voir au dessus
        b = np.array([res1,res2,res3]) # voir au dessus
        x = np.linalg.solve(a, b) # voir au dessus
        print("=============================================") # Encore un print
        print("Vos inconnues sont respectivement égales à", x) # Encore un print mais lui il affiche les résultats de vos inconnues
        print("=============================================") # Encore un print
if nbEqua == 4:
        #-----------------------------------------------Sous-Partie de la première équation---------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("[1ERE EQUATION] Entrez la valeur de la première inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val1 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[1ERE EQUATION] Entrez la valeur de la deuxième inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val2 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[1ERE EQUATION] Entrez la valeur de la troisième inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val3 = int(input()) # voir au dessus
        print ("[1ERE EQUATION] Entrez la valeur de la quatrième inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val4 = int(input()) # voir au dessus

#-----------------------------------------------Sous-Partie de la deuxième équation----------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("[2EME EQUATION] Entrez la valeur de la première inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val5 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[2EME EQUATION] Entrez la valeur de la deuxième inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val6 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[2EME EQUATION] Entrez la valeur de la troisième inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val7 = int(input()) # voir au dessus
        print ("[2EME EQUATION] Entrez la valeur de la quatrième inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val8 = int(input()) # voir au dessus

#-----------------------------------------------Sous-Partie de la troisième équation---------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("[3EME EQUATION] Entrez la valeur de la première inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val9 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[3EME EQUATION] Entrez la valeur de la deuxième inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val10 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[3EME EQUATION] Entrez la valeur de la troisième inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val11 = int(input()) # voir au dessus
        print ("[3EME EQUATION] Entrez la valeur de la quatrième inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val12 = int(input()) # voir au dessus

#-----------------------------------------------Sous-Partie de la quatrième équation---------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("[4EME EQUATION] Entrez la valeur de la première inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val13 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[4EME EQUATION] Entrez la valeur de la deuxième inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val14 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[4EME EQUATION] Entrez la valeur de la troisième inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val15 = int(input()) # voir au dessus
        print ("[4EME EQUATION] Entrez la valeur de la quatrième inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val16 = int(input()) # voir au dessus

#------------------------------------------------Sous-Partie des résultats-------------------------------------------------------------------------- 

        print("-----------------------------------------------") # Encore un print
        print ("[RESULTAT 1] Entrez le résultat de la première équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res1 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[RESULTAT 2] Entrez le résultat de la deuxième équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res2 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print("[RESULTAT 3] Entrez le résultat de la troisième équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res3 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("[RESULTAT 4] Entrez le résultat de la quatrième équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res4 = int(input()) # voir au dessus
        a = np.array([[val1,val2,val3,val4], [val5,val6,val7,val8], [val9,val10,val11,val12], [val13,val14,val15,val16]]) # voir au dessus
        b = np.array([res1,res2,res3,res4]) # voir au dessus
        x = np.linalg.solve(a, b) # voir au dessus
        print("=============================================") # Encore un print
        print("Vos inconnues sont respectivement égales à", x) # Encore un print mais lui il affiche les résultats de vos inconnues
        print("=============================================") # Encore un print
if nbEqua > 4:
        print ("Non pris en charge actuellement.")

