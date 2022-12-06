g = lambda: [*map(int, input().split())]

N = int(input())
p = [g() for _ in range(N)]
M = int(input())
S = set(g())
cnt = 0
for i in range(N):
    a, b = p[i]
    if a and b:
        cnt += all(c not in S for c in [a, b, i+1])
print(cnt)