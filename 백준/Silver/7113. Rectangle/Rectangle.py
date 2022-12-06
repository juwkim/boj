ans = 0
n, m = sorted(map(int, input().split()))
while n:
    ans += 1
    n, m = sorted([n, m - n])
print(ans)