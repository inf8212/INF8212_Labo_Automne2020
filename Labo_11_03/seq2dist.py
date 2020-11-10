"""
seq2dist est un script qui génère une matrice de distance pour un jeu de données de séquences en format Phylip séquentiel.
Les données sont lues dans un fichier .phy
Les résultats sont écris dasn un fichier .dist
La distance de Hamming est calculée pour chaque paire de séquence.

Auteur  : Alix Boc
Date    : Automne 2020
version : 1.0
"""

import sys


def distanceHamming(s, t):
    if len(s) != len(t):
        print('Les séquences ne sont pas de même taille. Arrêt.')
        exit()
    distance = 0
    for i in range(len(s)):
        if s[i].upper() != t[i].upper():  # <- J'ai ajouté la méthode upper() pour désensibiliser à la casse (i.e. ne pas tenir compte de maj/min)
            distance += 1
    return distance # Retourne un entier

def lecture_sequences(fichier):
    IN = open(fichier,"r")
    IN.readline() # on lit la première ligne avant de rentrer dans la boucle pour s'en débarrasser
    sequences = {}
    for ligne in IN:
        tab_ligne = ligne.split(" ")
        sequences[tab_ligne[0]] = tab_ligne[1][:-1] # on prend tout sauf le dernier caractères (retour à la ligne)
    IN.close()
    return sequences # Retourne un dictionnaire

def seqToDist(sequences):
    # Initialisation de la matrice, en utilisant la technique des compréhension de liste
    matrice = [[0]*len(sequences) for _ in sequences]
    # On change le dictionnaire des séquences en liste (avec les valeurs), comme ça on peut se servir de l'index
    sequences = list(sequences.values())
    # Itérations imbriquées (toutes les combinaisons de séquences entre-elles)
    for i in range(len(sequences)):
        for j in range(len(sequences)):
            if   i == j            : matrice[i][j] = 0              # On évite de calculer la diagonale, tjs égale à 0
            elif matrice[j][i] != 0: matrice[i][j] = matrice[j][i]  # On évite de calculer la même distance 2 fois (A vers B, B vers A)
            else                   : matrice[i][j] = distanceHamming(sequences[i], sequences[j])  # <- On appelle notre fonction de calcul de la distance!
    return matrice # Retourne une liste de listes

def sauvegarder_matrice_distances(fichier, sequences, matrice):
    # On change le dictionnaire des séquences en liste (avec les clés), comme ça on peut se servir de l'index
    sequences = list(sequences)
    # Créer fichier. 1ere ligne avec le nombre de séquences (d'espèces)
    f = open(fichier, 'w')
    print(len(matrice[0]), file=f)
    # Pour chaque ligne dans la matrice...
    for index, ligne in enumerate(matrice):
        # On transforme les entiers en chaîne de caractères
        for i in range(len(ligne)): ligne[i] = str(ligne[i])
        # On ajoute le nom de l'espèce, on fait la concaténation des éléments de la liste et on imprime dans le fichier
        ligne_str = sequences[index] + ' ' + ' '.join(ligne)
        print(ligne_str, file=f)
    f.close()



"""
    PROGRAMME PRINCIPAL
"""

#= Lecture des arguments de la ligne de commande
if len ( sys.argv ) != 3:
    print ( "option illegale" )
    print ( "usage :",sys.argv[0],"input.phy output.txt" )
    sys.exit(-1)

# Appel des fonctions
sequences = lecture_sequences ( sys.argv[1] )
matrice_distances = seqToDist ( sequences )
sauvegarder_matrice_distances ( sys.argv[2], sequences, matrice_distances )
print ( "\nFin normale du programme\n" )