################################################
# Déterminer si une année est bissextile
# Exercice pour INF8212
# 22 sept 2020
################################################


# Entrée utilisateur
annee = int(input('Inscrivez une année :'))

# Conditions
condition1 = (annee %4   == 0) and (annee %100 != 0)
condition2 = (annee %400 == 0)

# Évaluation et message utilisateur
if condition1 or condition2: print(annee, """est une année bissextile! :)""")
else                       : print(annee, """n'est pas une années bissextile :(""")
