import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M, K = g()
ans = 0
for _ in range(N):
    s = input()
    cur = s[:K].count('0')
    if cur == K:
        ans += 1
    for i in range(K, M):
        cur += (s[i] == '0') - (s[i - K] == '0')
        if cur == K:
            ans += 1
print(ans)