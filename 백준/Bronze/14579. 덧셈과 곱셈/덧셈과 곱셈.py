a, b = map(int, input().split())
ans = a * (b + 1)
for i in range(a + 1, b + 1):
    ans *= i**2
print(ans // 2**(b - a + 1) % 14579)