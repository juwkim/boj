num = abs(int(input())) + 1
if num & (num - 1):
    print(-1)
else:
    ans = -1
    while num:
        ans += 1
        num >>= 1
    print(ans)