```python
rows = int(input())
cols = int(input())

matrix1 = []
matrix2 = []
result = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)

for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)

for i in range(rows):
    result.append([matrix1[i][j] + matrix2[i][j] for j in range(cols)])

for row in result:
    print(' '.join(map(str, row)))
```