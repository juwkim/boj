g = lambda: [*map(int, input().split())]

r, c = g()
rows = [input() for _ in range(10)]
row = [i+1 for i in range(10) if len(set(rows[i])) == 1]
cols = [*zip(*rows)]
col = [i+1 for i in range(10) if len(set(cols[i])) == 1]
print(min(abs(r - i) for i in row) + min(abs(c - i) for i in col))