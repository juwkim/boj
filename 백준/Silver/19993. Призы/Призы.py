n, m = sorted(map(int, input().split()))
if n == 1:
    ans = (m + 1) // 4
elif n == 2:
    ans = 0
else:
    ans = 1
print(ans)