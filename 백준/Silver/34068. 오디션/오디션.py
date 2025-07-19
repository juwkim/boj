import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
score = [0] * N
for _ in range(M):
    A, B = g()
    score[A - 1] += 1
l = [0] * (M + 1)
for i in range(N):
    l[score[i]] += 1
ans = 0
for i in range(M):
    cnt = max(l[i] - 1, 0)
    l[i + 1] += cnt
    ans += cnt
ans += l[M] * (l[M] - 1) >> 1
print(ans)