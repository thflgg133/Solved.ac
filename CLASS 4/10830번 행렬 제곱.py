import sys

def mulmatrix(m1, m2):
    tmp =  [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += m1[i][k] * m2[k][j]
                tmp[i][j] %= 1000
         
    return tmp


def devide(b, matrix):
    if b == 1:
        return matrix

    else:
        if b % 2 == 0:
            matrix = devide(b//2, matrix)
            return mulmatrix(matrix, matrix)

        else:
            matrix = devide(b-1, matrix)
            return mulmatrix(first_matrix, matrix)


N, B = map(int, sys.stdin.readline().split())
first_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for col in range(N):
    for row in range(N):
        print(devide(B, first_matrix)[col][row] % 1000, end =" ")
    print()