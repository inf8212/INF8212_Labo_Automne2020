def apparimentsEtendus(s, t):
    
    n = len(s)
    if len(t) != n: return None

    dictionnary = {}   # Va servir à stocker les positions de t pour les valeurs de s (les valeurs de s sont les clés du dictionnaire)
    positions   = []   
    for i in range(n):
        if s[i] not in dictionnary:
            dictionnary[s[i]] = []
            for j in range(n):
                if t[j] == s[i]:
                    dictionnary[s[i]].append(j)
                    positions.append((i, j))
        else:
            for j in dictionnary[s[i]]:
                positions.append((i, j))
                            
            
    return positions