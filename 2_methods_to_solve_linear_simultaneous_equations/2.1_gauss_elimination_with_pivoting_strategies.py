system = [
    [3,     -0.1,   -0.2,        7.85 ],
    [0.1,    7,     -0.3,       -19.3],
    [0.3,   -0.2,    10,         71.4 ]
]

def forward_elimination(sys):
    n = len(sys)
    for k in range(0, n-1):
        for i in range(k+1, n):
            factor = sys[i][k] / sys[k][k]
            for j in range(k+1, n+1):
                sys[i][j] = sys[i][j] - factor * sys[k][j]
    return sys

def back_substitution(sys):
    n = len(sys)
    solution = [0] * n
    solution[n-1] = sys[n-1][n] / sys[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = sys[i][n]
        for j in range(i+1, n):
            sum -= sys[i][j] * solution[j]
        solution[i] = sum / sys[i][i]
    return solution




if __name__ == "__main__":
    
    forward_eliminated = forward_elimination(system)
    # for i in range(0, len(forward_eliminated)):
    #     print(forward_eliminated[i])
    back_substituted = back_substitution(forward_eliminated)
    print("\n| --- Solution --- |")
    print(back_substituted)