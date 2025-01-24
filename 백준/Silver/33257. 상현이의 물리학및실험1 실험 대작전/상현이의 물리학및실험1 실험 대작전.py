N, E, *D = map(int, open(0).read().split())
ans, prv = 0, -1e9
for num in sorted(D):
    if num >= prv + E:
        ans += 1
    prv = num
print(ans)