g = lambda: [*map(int, input().split())]

N, L = g()
ans = 0
cur = None

for num in sorted(g()):
    if cur == None or num - cur >= L:
        ans += 1
        cur = num
print(ans)