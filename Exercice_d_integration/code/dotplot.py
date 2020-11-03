from matplotlib import pyplot as plt

def dotplot(positions):
    
    # On transforme d'abord les paires (i, j) en listes de coordonnées x et y
    x, y = list(), list()
    for index in positions:
        x.append(index[0])
        y.append(index[1])
    
    # On peut ensuite afficher les points dans un graphique (scatter() = nuage de points)
    plt.scatter(x, y, s=25)  # Cré un graphique de type 'Scatter plot'. Option 's' pour la taille des points
    plt.show()               # Affiche le graphique à l'écran!
    plt.clf()                # Efface le graphique de la mémoire