n, *A = map(int, open(0).read().split())
ans, need = 0, 2
l = 2 ** -.75
for num in A:
    ans += l * need / 2
    l /= 2 ** .5
    if num >= need:
        break
    need = (need - num) << 1
else:
    ans = "impossible"
print(ans)