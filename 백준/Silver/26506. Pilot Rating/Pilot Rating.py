n, *l = map(int, open(0))
l.sort()
ans = min(l[i] + l[-(i+1)] for i in range(n>>1))
print(ans)