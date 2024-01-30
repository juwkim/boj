ans = 0
n = int(input())
cur = 2
while cur <= n:
    num = cur
    while num <= n:
        ans += 1
        num *= 3
    cur *= 2
print(ans)