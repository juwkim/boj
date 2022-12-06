while int(N := input()):
    while len(N) > 1:
        N = str(sum(map(int, N)))
    print(N)