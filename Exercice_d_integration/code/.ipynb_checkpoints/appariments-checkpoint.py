def appariments(s, t):
    
    n = len(s)
    if len(t) != n: return None

    positions = []
    for i in range(n):
        if s[i] == t[i]: positions.append(i)
    return positions