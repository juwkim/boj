L, R = map(int, input().split())
ans = 0
for i in range(1, R + 1):
    ans += i * (R // i - (L + i - 1) // i + 1)
print(ans)