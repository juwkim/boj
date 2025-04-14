import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
cnt = [0] * N
for _ in range(M):
    cnt[max(g()) - 1] += 1
ans = []
for i in range(1, N):
    if cnt[i] == 0:
        ans.append('N')
    elif cnt[i] == i:
        ans.append('E')
    else:
        ans = [-1]
        break
print(*ans, sep='')