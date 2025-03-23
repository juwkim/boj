import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

mats = []
n = int(input())
for _ in range(n):
    r, c = g()
    mats.append([g() for _ in range(r)])
A = mats[0]
for i in range(1, n):
    B = mats[i]
    C = []
    for r1 in A:
        for r2 in B:
            l = []
            for a in r1:
                for b in r2:
                    l.append(a * b)
            C.append(l)
    A = C
print(max(map(max, A)))
print(min(map(min, A)))
row_sum = [sum(r) for r in A]
print(max(row_sum))
print(min(row_sum))
col_sum = [sum(c) for c in zip(*A)]
print(max(col_sum))
print(min(col_sum))