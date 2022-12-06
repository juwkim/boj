ans = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans += 1 + max(0, b - ans % (a + b))
print(ans)