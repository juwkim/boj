for _ in range(int(input())):
    R, C = map(int, input().split())
    Map = [[0] * (C + 1)] + [[0] + [*map(int, input())] for _ in range(R)]
    ans = (R + 1) * (C + 1) - sum(line.count(0) for line in Map)
    ans += sum(sum(max(0, b - a) for a, b in zip(line, line[1:])) for line in Map)
    ans += sum(sum(max(0, b - a) for a, b in zip(line, line[1:])) for line in zip(*Map))
    print(ans * 2)