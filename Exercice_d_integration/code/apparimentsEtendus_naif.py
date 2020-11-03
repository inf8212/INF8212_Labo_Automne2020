def apparimentsEtendus_naif(s, t):
    
    n = len(s)
    if len(t) != n: return None               

    positions = []
    for index_s, value_s in enumerate(s):
        for index_t, value_t in enumerate(t):
            if value_s == value_t: positions.append((index_s, index_t))
            
    return positions