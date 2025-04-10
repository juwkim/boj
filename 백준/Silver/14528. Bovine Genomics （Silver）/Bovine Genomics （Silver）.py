import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]
ans = 0
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            s = set(l[i] + l[j] + l[k] for l in A)
            t = set(l[i] + l[j] + l[k] for l in B)
            if not s & t:
                ans += 1
print(ans)