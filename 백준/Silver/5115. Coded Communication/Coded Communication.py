g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    n, b = g()
    buf = [input() for _ in range(n)]
    s = input()
    ans = min(sum(a != b for a, b in zip(s, l)) for l in buf)
    print(f'Data Set {_}:\n{ans}\n')