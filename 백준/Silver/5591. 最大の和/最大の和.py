g = lambda: [*map(int, input().split())]

px = [0]
n, k = g()
for _ in range(k-1):
    px.append(px[-1] + int(input()))
ans = 0
for _ in range(n-k+1):
    px.append(px[-1] + int(input()))
    ans = max(ans, px[-1] - px[-1-k])
print(ans)