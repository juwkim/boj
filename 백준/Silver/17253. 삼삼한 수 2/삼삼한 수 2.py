N = int(input())
if N == 0:
    ans = "NO"
else:
    ans = "YES"
    while True:
        N, r = divmod(N, 3)
        if r == 2:
            ans = "NO"
            break
        if N == 0:
            break
print(ans)