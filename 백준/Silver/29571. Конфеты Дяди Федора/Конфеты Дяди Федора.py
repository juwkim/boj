n = int(input())
cur = 0
l, r = 45000, 45000
while cur != n and l >= r and r > 1:
    if cur < n:
        cur += r * (r + 1) // 2
        r -= 1
    elif cur > n:
        cur -= l * (l + 1) // 2
        l -= 1
print(("NO", "YES")[cur == n])