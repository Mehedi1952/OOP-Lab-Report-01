rows1 = int(input())
cols1 = int(input())
rows2 = int(input())
cols2 = int(input())

matrix1 = []
matrix2 = []
result = [[0 for _ in range(cols2)] for _ in range(rows1)]

for i in range(rows1):
    row = list(map(int, input().split()))
    matrix1.append(row)

for i in range(rows2):
    row = list(map(int, input().split()))
    matrix2.append(row)

for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for row in result:
    print(' '.join(map(str, row)))
