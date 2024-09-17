n, r = map(int, input().split())
r -= 1
ans, i = n, 1 << n - 1
while r > i:
    r -= i
    ans -= 1
    i >>= 1
print(ans)