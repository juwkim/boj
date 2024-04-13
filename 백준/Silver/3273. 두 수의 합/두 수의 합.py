n = int(input())
a = sorted(map(int, input().split()))
x = int(input())
ans, l, r = 0, 0, n - 1
while l < r:
    num = a[l] + a[r]
    if num == x: ans += 1; l += 1; r -= 1
    elif num > x: r -= 1
    else: l += 1
print(ans)