g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    input()
    r, c = g()
    Map = [input() for _ in range(r)]
    ans = sum(line.count('>o<') for line in Map)
    ans += sum(''.join(line).count('vo^') for line in zip(*Map))
    print(ans)