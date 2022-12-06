g = lambda: [*map(int, input().split())]

r, c = g()
row = [0, r]
col = [0, c]
for _ in range(int(input())):
    a, b = g()
    if a:
        row.append(b)
    else:
        col.append(b)
row.sort()
col.sort()
s = max(j - i for i, j in zip(row, row[1:]))
t = max(j - i for i, j in zip(col, col[1:]))
print(s * t)