#####################################################
# Exemple d'implémentation de matrices 5x5
#####################################################


# Matrices avec des listes de listes
#####################################################

# Bonne façon d'implémenter
lsta = []
for i in range(5):
    lsta.append([])
    for _ in range(5):
        lsta[i].append(0)
print(lsta); lsta[4][4] = 1; print(lsta)


# Bonne façon d'implémenter; avec compréhension de liste
lstb = [[0 for i in range(5)] for i in range(5) ]
print(lstb); lstb[4][4] = 1; print(lstb)



# PAS ok
lst1 = [0, 0, 0, 0, 0]
lst2 = [lst1 for i in range(5) ]
print(lst2); lst2[4][4] = 1; print(lst2)

# PAS ok
lst3 = [[0]*5]*5
print(lst3); lst3[4][4] = 1; print(lst3)





# Matrices avec numpy
#####################################################
import numpy as np

matrix = np.zeros((5, 5))
print(matrix); matrix[4][4] = 1; print(matrix)
