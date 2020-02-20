

def doolittle_decomposition(a):
    n = len(a)    
    for k in range(0, n-1):
        for i in range(k+1, n):
            factor = a[i][k] / a[k][k]
            a[i][k] = factor
            for j in range(k+1, n):
                a[i][j] -= factor * a[k][j]
    return a

def forward_back_substitution(a, b):
    # forward substitution
    n = len(a)
    for i in range (1, n):
        sum = b[i]
        for j in range(0, i):
            sum -= a[i][j] * b[j]
        b[i] = sum
    # back substitution
    x = [0] * n
    x[n-1] = b[n-1] / a[n-1][n-1]
    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += a[i][j] * x[j]
        x[i] = (b[i]-sum)/a[i][i]
    return x

if __name__ == "__main__":
    a = [
        [3,     -0.1,   -0.2],
        [0.1,    7,     -0.3],
        [0.3,   -0.2,    10 ]
    ]
    b =  [7.85, -19.3, 71.4 ]

    lu = doolittle_decomposition(a)
    print("| --- LU Decomp --- |")
    for i in range(0,len(lu)):
        print(lu[i])
    print("| --- Solution --- |")
    print(forward_back_substitution(lu, b))