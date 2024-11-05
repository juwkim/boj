n = int(input())
ans, v = 0, 0
for _ in range(n):
    x, r, c = map(int, input().split())
    ans += x > v
    v = x + r * c
print(ans)