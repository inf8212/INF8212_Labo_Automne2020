def appariments(s, t):
    
    n = len(s)
    if len(t) != n: return None

    positions = []
    for i in range(n):
        if s[i].upper() == t[i].upper(): positions.append(i)
    return positions