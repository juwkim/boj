g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    s = input()
    input()
    cur = 0
    for num in g():
        cur += num
        print(s[cur % len(s)], end='')
    print()