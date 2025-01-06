import sys
input = sys.stdin.readline

n = int(input())
r, g = zip(*[[*map(int, input().split())] for _ in range(n)])
ans = -1
for i in range(1, 1000000):
    if all(i % (r[j] + g[j]) >= r[j] for j in range(n)):
        ans = i
        break
print(ans)