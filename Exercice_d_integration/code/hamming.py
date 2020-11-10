def hamming(s, t):
    
    n = len(s)
    if len(t) != n: return None

    distance = 0
    for i in range(n):
        if s[i].upper() != t[i].upper(): distance += 1
            
    return distance