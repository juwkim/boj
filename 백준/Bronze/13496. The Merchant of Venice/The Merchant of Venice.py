g = lambda: [*map(int, input().split())]

for i in range(1, 1 + int(input())):
    n, s, day = g()
    ans = 0
    for _ in range(n):
        d, v = g()
        if d <= s * day:
            ans += v
    print(f'Data Set {i}:\n{ans}\n')