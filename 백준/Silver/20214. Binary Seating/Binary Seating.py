n, *l = map(int, open(0).read().split())
ans, mul = 0, .5
for num in sorted(l, reverse=True):
    ans += num * mul
    mul /= 2
print(ans)