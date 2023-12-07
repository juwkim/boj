from math import gcd

N, M, *l = map(int, open(0).read().split())
ans = 'No'
g = N
for num in l:
    g = gcd(g, num)
    if g == 1:
        ans = 'Yes'
        break
print(ans)