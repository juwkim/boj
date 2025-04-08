import sys
input = sys.stdin.readline

N = int(input())
L, G = [], []
for _ in range(N):
    s, x = input().split()
    x = int(x)
    if s == 'L':
        L.append(x)
    else:
        G.append(x)
ans = N
for x in set(L + G):
    ans = min(ans, sum(p < x for p in L) + sum(p > x for p in G))
print(ans)