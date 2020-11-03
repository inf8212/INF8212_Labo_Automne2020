def seuil(toutesPositions, k):
    
    positions = []
    p = set(toutesPositions) # Les ensembles (set) sont comme des dictionnaires mais avec seulement des clés, pas de valeur
    for (i, j) in toutesPositions:
        kmer = []
        z = 0
        while z >= 0:
            coord = (i+z, j+z)
            if coord not in p: break
            kmer.append(coord)
            p.remove(coord)
            z += 1
        if len(kmer) >= k: positions += kmer
            
    return positions