for _ in range(int(input())):
    _, s, l = input().split("'")
    a, b, c, d = map(int, l.split())
    area = c * (2 * a + 2 * b + 3) + b * (a + 3) * 2
    ans = str(area)[:d] + '0' * (len(str(area)) - d)
    print(f"{s} requires {ans} square frightometers of paper to wrap")