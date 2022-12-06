g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    n, m = g()
    stations = [g() for _ in range(n)]
    visits = [stations[i-1] for i in g()]
    x_pos, y_pos = zip(*visits)
    
    x_min, x_max = min(x_pos), max(x_pos)
    y_min, y_max = min(y_pos), max(y_pos)
    
    ans = 0
    for station in stations:
        x, y = station
        if x_min <= x <= x_max and y_min <= y <= y_max:
            ans += 1
    print(f'Data Set {cnt}:\n{ans}\n')