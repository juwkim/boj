g = lambda: [*map(int, input().split())]


for cnt in range(1, 1 + int(input())):
    n, W, E = g()
    ans = 0
    for _ in range(n):
        a, b, c, d = g()
        ans += max(W*a + E*c, W*b + E*d)
    print(f'Data Set {cnt}:\n{ans}\n')