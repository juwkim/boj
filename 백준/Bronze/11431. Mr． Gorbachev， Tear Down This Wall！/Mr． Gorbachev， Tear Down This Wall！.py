g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    n, s, p = g()  
    ans = 0
    points = [g() for _ in range(n+1)]
    for i in range(n):
        x, y = points[i]
        a, b = points[i+1]
        ans += abs(x - a) + abs(y - b)
    ans = (ans * s + p - 1) // p
    print(f'Data Set {cnt}:\n{ans}\n')