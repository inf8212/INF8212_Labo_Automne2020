def affichageAlignement(s, t, positions):
    
    # Chaîne 'pipes' des caractères de formattage,  vide pour commencer
    pipes = str()
    
    # Construction de la chaîne pipes
    n = len(s)
    for i in range(n):
        if i in positions: pipes += '|'
        else:              pipes += ' '
    
    # Affichage des 3 chaînes les unes sous les autres (avec sep='\n').
    print('\n', s, pipes, t, sep='\n')