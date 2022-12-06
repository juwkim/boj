n, m = map(int, input().split())

rows = [input().split() for _ in range(n)]
cols = [*zip(*rows)]

row_9 = [''.join(row).count('9') for row in rows]
col_9 = [''.join(col).count('9') for col in cols]

print(sum(row_9) - max(row_9 + col_9))