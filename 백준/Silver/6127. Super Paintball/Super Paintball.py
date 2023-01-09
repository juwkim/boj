input = __import__('sys').stdin.readline
def g(): return map(int, input().split())

N, K = g()
cows = set(tuple(g()) for _ in range(K))

ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        ans += all(i == x or j == y or i - j == x - y or i + j == x + y for x, y in cows)
print(ans)