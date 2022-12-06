n = int(input()) + 1
ans = 0
for i in range(1, int(n**.5)+1):
    r, q = divmod(n, i)
    if q == 0:
        if r == i:
            ans += 1
        else:
            ans += 2

print(ans)