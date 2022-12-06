from math import gcd
D1, D2 = map(int, input().split())
ans = 1
for i in range(D1, D2 + 1):
    for j in range(1, i):
        num = gcd(j, i)
        if num == 1 or i - i // num < D1:
            ans += 1
print(ans)