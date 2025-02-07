n, *A = map(int, open(0).read().split())
ans, need, l = 0, 2, -1.75
for num in A:
    ans += need * 2 ** l
    if num >= need:
        break
    need = need - num << 1
    l -= .5
else:
    ans = "impossible"
print(ans)