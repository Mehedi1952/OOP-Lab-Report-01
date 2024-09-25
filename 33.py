```python
rows = int(input())
cols = int(input())

matrix = []
transpose = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

for row in transpose:
    print(' '.join(map(str, row)))
```