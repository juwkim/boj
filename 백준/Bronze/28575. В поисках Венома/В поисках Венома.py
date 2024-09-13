a, b = sorted(map(int, input().split()))
ans = 0
while a:
    ans += b // a
    a, b = b % a, a
print(ans)