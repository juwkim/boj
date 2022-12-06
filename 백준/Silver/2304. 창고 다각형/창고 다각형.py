g = lambda: [*map(int, input().split())]

N = int(input())
pos, h = zip(*sorted([g() for _ in range(N)], key=lambda x: -x[1]))
l, r = pos[0], pos[0]
s, e = min(pos), max(pos)

ans = h[0]
for i in range(1, N):
    
    if l < pos[i] < r:
        continue
    
    if pos[i] > r:
        ans += h[i] * (pos[i] - r)
        r = pos[i]
    else:
        ans += h[i] * (l - pos[i])
        l = pos[i]

    if s == l and e == r:
        break
    
print(ans)