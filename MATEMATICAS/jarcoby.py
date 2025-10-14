A = [
     [4, 1, -1, 3],
     [2, 5, 1, 6],
     [1, 1, 3, 4]
    ]

n = 3
N=10
x = [0] * n
xn = [0] * n

for k in range(N):
    for i in range(n):
        sum = 0
        for j in range(n):
            if i!=j:
                sum += A[i][j] * xn[j]
        xn[i] = (A[i][n] - sum) / A[i][i]
        x[i] = xn[i]
    print(x)


