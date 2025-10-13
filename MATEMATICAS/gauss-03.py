A = [[2,1,1,8],[-3,-1,2,-11],[-2,1,2,-3]]
n = 3
# n = 3
# para k = 1 hasta n hacer
#    Dividir fila k por akk para hacer pivote = 1
#    para i = 1 hasta n hacer
#       Si i != k entonces
#          Multiplicar fila i por aik y restar a fila i la fila k multiplicada por aik 
#       Fin Si
#    Fin Para
# Fin Para

#para k = 1 hasta n hacer
    #para i = 1 hasta n hacer
    #si i # k entonces
        #Dividir fila k por akk para hacer pivote = 1
        #m = aik
        #para j = k hasta n t 1 hacer
            # aij = aij - m * akj
        #fin para
    #fin si
#fin para

for k in range(0, n):
    for p in range(0, n+1):
        A[p][j] = A[p][j] - aik * A[k][k]
    for j in range(0, n):
        if i != k:
            m = A[i][k]
            for j in range(k, n+1):
                A[i][j] = A[i][j] - m * A[k][j]


for i in range(0, n):
    for j in range(0, n+1):
        A[i][j] = A[i][j] / A[i][i]

print(A)        

