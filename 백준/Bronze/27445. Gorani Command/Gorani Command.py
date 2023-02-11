def g(): return [*map(int, input().split())]

N, M = g()
row = [int(input()) for _ in range(N - 1)]
col = g()
row += [col[0]]

r = min(range(N), key=lambda x: row[x])
c = min(range(M), key=lambda x: col[x])
print(r + 1, c + 1)