n, *a = map(int, open(0).read().split())
a.sort()
ans, MOD = 1, 10**9 + 7
for i in range(n):
    slots = a[i] - (i + 1)
    if slots < 0:
        ans = 0
        break    
    ans = (ans * (slots + 1)) % MOD
print(ans)