###################################################################################
# Fibonacci numbers. Exemples de récursion et de mémoisation
# INF8212 - Automne 2020
# Mathieu Lemieux @ Université du Québec à Montréal
###################################################################################



# 1er exemple; récursion seulement
#########################################
def fib_recursion(n):
    if   n == 1: return 0
    elif n == 2: return 1
    else       : return fib_recursion(n-1) + fib_recursion(n-2)


# 2ème exemple; récursion avec mémoisation
#########################################
memo = dict()
def fib_memoisation(n):
    if   str(n) in memo: pass
    elif n == 1        : memo[str(n)] = 0
    elif n == 2        : memo[str(n)] = 1
    else               : memo[str(n)] = fib_memoisation(n-1) + fib_memoisation(n-2)
    return memo[str(n)]


# 3ème exemple; récursion avec mémoisation en utilisant le décorateur lru_cache
# Décorateur = Fonction qui prend comme paramètre une autre fonction.
# Ici, '@lru_cache' devant la définition de 'fib_memoisation_cache(n)' signifie que sur appel,
# la seconde va être passée en argument à la première.
#########################################
from functools import lru_cache
@lru_cache
def fib_memoisation_cache(n):
    if   n == 1: return 0
    elif n == 2: return 1
    else       : return fib_memoisation_cache(n-1) + fib_memoisation_cache(n-2)


# 4ème exemple; récursion avec mémoisation en utilisant un décorateur fait maison
#########################################
def deco(func):
    memo = dict()
    def inner(n):
        if str(n) in memo: return memo[str(n)]
        else             : memo[str(n)] = func(n)
        return memo[str(n)]
    return inner

@deco
def fib_memoisation_deco(n):
    if   n == 1: return 0
    elif n == 2: return 1
    else       : return fib_memoisation_deco(n-1) + fib_memoisation_deco(n-2)



# Start of program
###################################################################################
if __name__ == '__main__':

    # On prend les paramètres via la console lors de l'exécution du programme.
    # Ex. 'python fibonacci.py 33 m', où gen=33 et algo=mémoisation
    
    import sys

    # Nb de générations (défaut = 10)
    if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 1: n = int(sys.argv[1])
    else                                                                       : n = 10

    # Algorithme choisi (défaut = Récursion)
    if len(sys.argv) >= 3:
        if   sys.argv[2] == 'm': print(f'Fibionacci de {n} avec mémoisation = {fib_memoisation(n)}')
        elif sys.argv[2] == 'c': print(f'Fibionacci de {n} avec lru_cache = {fib_memoisation_cache(n)}')
        elif sys.argv[2] == 'd': print(f'Fibionacci de {n} avec décorateur = {fib_memoisation_deco(n)}')
        else                   : print(f'Fibionacci de {n} avec récursion seulement = {fib_recursion(n)}')
    else                       : print(f'Fibionacci de {n} avec récursion seulement = {fib_recursion(n)}')
