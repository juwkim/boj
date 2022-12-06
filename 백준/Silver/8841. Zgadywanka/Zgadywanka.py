g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    Z, K = g()
    ans = 0
    while Z:
        ans += 1
        Z //= K + 1
    print(ans)