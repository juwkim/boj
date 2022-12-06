for _ in range(int(input())):
    s = map(lambda x: round(sum(x)/10 + 0.01), zip(*[[*map(int, input().split())] for _ in range(10)]))
    print(*s)