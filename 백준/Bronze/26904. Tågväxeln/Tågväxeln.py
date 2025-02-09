n, m = map(int, input().split())
ans = 1439 // m * 2
if 1439 - 1439 % m >= 1439 // n * n:
    ans -= 1
print(ans)