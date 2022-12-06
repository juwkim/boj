g = lambda: [*map(int, input().split())]

while True:
    try:
        N, S = g()
        print(S // (N + 1))
    except:
        break