g = lambda: [*map(int, input().split())]

P, N = g()

ans = 0
for num in sorted(g()):
    if P < 200:
        P += num
        ans += 1
    else:
        break
print(ans)