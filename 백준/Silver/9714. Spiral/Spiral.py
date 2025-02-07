for N in map(int, [*open(0)][1:]):
    def solve():
        x, y = 0, 0
        num, d = 1, 1
        while True:
            if num + d >= N:
                y += N - num
                return f"({x},{y})"
            y += d
            num += d
            if num + d >= N:
                x += N - num
                return f"({x},{y})"
            x += d
            num += d
            d += 1
            if num + d >= N:
                y -= N - num
                return f"({x},{y})"
            y -= d
            num += d
            if num + d >= N:
                x -= N - num
                return f"({x},{y})"
            x -= d
            num += d
            d += 1
    print(solve())