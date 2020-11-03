def affichageAlignement_v2(s, t, positions, width=60):
    
    # Cette fois-ci, utilisation de 'compréhension de liste' pour générer la chaîne 'pipes'
    n = len(s)
    pipes = ''.join(['|' if i in positions else ' ' for i in range(n)])
    
    # Nombre de lignes selon le nombre de caractères alloués par ligne
    nbLines = n//width if n%width==0 else (n//width)+1  # Nb. de lignes
    
    # Formattage ligne par ligne
    for i in range(nbLines):
        _s     =     s[i*width:(i+1)*width]
        _t     =     t[i*width:(i+1)*width]
        _pipes = pipes[i*width:(i+1)*width]
        print('\n', _s, _pipes, _t, sep='\n')