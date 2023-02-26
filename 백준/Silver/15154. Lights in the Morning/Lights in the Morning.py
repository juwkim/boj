ans = 'YES'
N, D = map(int, input().split())
for _ in range(N):
    x, a, g, r = map(int, input().split())
    s = (x - a) % (g + r)
    if x < a or s > g:
        ans = 'NO'
        break
print(ans)