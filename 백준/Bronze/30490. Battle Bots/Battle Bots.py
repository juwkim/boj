ans = 1
n = int(input()) - 1
while n:
    n >>= 1
    ans += 1
print(ans)