
def crout_decomposition(a):
    n = len(a)
    for j in range(1, n):
        a[1][j] = a[1][j]/a[1][1]
    for j in range(1, n-1):
        for i in range(j, n):
            sum = 0
            for k in range(0, j-1):
                sum += a[i][k] * a[k][j]
            a[i][j] -= sum
        for k in range(j+1, n):
            sum = 0
            for i in range(0, j-1):
                sum += a[j][i] * a[i][k]
            a[j][k] = (a[j][k] - sum)/a[j][j]
        sum = 0
        for k in range(0, n-1):
            sum += a[n-1][k] * a[k][n-1]
    a[n-1][n-1] -= sum
    return a

if __name__ == "__main__":
    a = [
        [3,     -0.1,   -0.2],
        [0.1,    7,     -0.3],
        [0.3,   -0.2,    10 ]
    ]
    b =  [7.85, -19.3, 71.4 ]

    ul = crout_decomposition(a)
    for row in ul:
        print(row)