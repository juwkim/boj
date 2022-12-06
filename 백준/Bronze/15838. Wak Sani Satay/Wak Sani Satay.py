g = lambda: [*map(int, input().split())]
cnt = 1
while n := int(input()):
    ans = 0
    for _ in range(n):
        chicken, beef, lamb, nasi = g()
        ans += 0.8 * chicken + 1 * beef + 1.2 * lamb + 0.8 * nasi
        ans -= chicken / 85 * 15.5
        ans -= beef / 85 * 32
        ans -= lamb / 85 * 40
        ans -= nasi * 0.2
    print(f'Case #{cnt}: RM{ans:.2f}')
    cnt += 1