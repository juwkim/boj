n, *l = map(int, open(0))
l.sort()
ans = sum(l)
for i in range(n//2):
    ans += l[-i-1] - l[i]
print(ans)