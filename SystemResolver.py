import numpy as np # Importation de la bilbiothèque "numpy"


# SystemResolver est un script Python permettant de résoudre des systèmes à 2 ou 3 équations (et surement plus dans le futur)
# Créé par LeCoqHardi, disponible sur Github. 

print("================[SystemResolver]================") # Bon en gros les print ça affiche voilà 
print("Combien votre système contient-il d'équations ?") # Encore un print 
nbEqua = int(input()) # Variable du nombre d'équations du système

#-----------------------------------------------Super-Partie des équations à 2 inconnues---------------------------------------------------------

if nbEqua == 2: # Dois-je réellement expliquer la fonction if ? Bah en gros ça test votre réponse, et si elle est égale à celle dans sa condition vous rentrez dans sa boucle
    print("-----------------------------------------------") # Encore un print 
    print("Combien votre système contient-il d'inconnues ?") # Encore un print
    print("-----------------------------------------------") # Encore un print
    nbInco = int(input()) # Variable du nombre d'inconnues dans les équations du système

#-------------------------------------------------Partie des équations à 2 inconnues-------------------------------------------------------------

    if nbInco == 2: # Encore un if

#-------------------------------------------------Sous-Partie de la première équation------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la première inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val1 = int(input()) # Variable contenant la valeur de la première inconnue de la première équation
        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la deuxième inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val2 = int(input()) # Variable contenant la valeur de la dexième inconnue de la première équation

#-------------------------------------------------Sous-Partie de la deuxième équation------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la première inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val3 = int(input()) # Variable contenant la valeur de la première inconnue de la deuxième équation
        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la deuxième inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val4 = int(input()) # Variable contenant la valeur de la dexième inconnue de la deuxième équation

#-------------------------------------------------Sous-Partie des résultats----------------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("Entrez le résultat de la première équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res1 = int(input()) # Variable contenant le résultat de la première équation
        print("-----------------------------------------------") # Encore un print
        print ("Entrez le résultat de la deuxième équation") # Encore un print
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
    print("-----------------------------------------------") # Encore un print
    print("Combien votre système contient d'inconnues ?") # Encore un print
    print("-----------------------------------------------") # Encore un print
    nbInco = int(input()) # Variable du nombre d'inconnues dans les équations du système
    if nbInco == 3: # Encore un if

#-----------------------------------------------Sous-Partie de la première équation---------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la première inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val1 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la deuxième inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val2 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la troisième inconnue de la première équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val3 = int(input()) # voir au dessus

#-----------------------------------------------Sous-Partie de la deuxième équation----------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la première inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val4 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la deuxième inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val5 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la troisième inconnue de la deuxième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val6 = int(input()) # voir au dessus

#-----------------------------------------------Sous-Partie de la troisième équation---------------------------------------------------------------

        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la première inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val7 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la deuxième inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val8 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("Entrez la valeur de la troisième inconnue de la troisième équation (sans la lettre)") # Encore un print
        print("-----------------------------------------------") # Encore un print
        val9 = int(input()) # voir au dessus

#------------------------------------------------Sous-Partie des résultats-------------------------------------------------------------------------- 

        print("-----------------------------------------------") # Encore un print
        print ("Entrez le résultat de la première équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res1 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print ("Entrez le résultat de la deuxième équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res2 = int(input()) # voir au dessus
        print("-----------------------------------------------") # Encore un print
        print("Entrez le résultat de la troisième équation") # Encore un print
        print("-----------------------------------------------") # Encore un print
        res3 = int(input()) # voir au dessus
        a = np.array([[val1,val2,val3], [val4,val5,val6], [val7,val8,val9]]) # voir au dessus
        b = np.array([res1,res2,res3]) # voir au dessus
        x = np.linalg.solve(a, b) # voir au dessus
        print("=============================================") # Encore un print
        print("Vos inconnues sont respectivement égales à", x) # Encore un print mais lui il affiche les résultats de vos inconnues
        print("=============================================") # Encore un print

