g = lambda: [*map(int, input().split())]

n, h = g()
ans = 0
while h:
    if n & 1:
        n = (n + 1) // 2
    else:
        n = n // 2
        ans += pow(2, h - 1)
    h -= 1
print(ans)