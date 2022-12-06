for _ in range(int(input())):
    t = [0, 0]
    for a, b in zip(*input().split()):
        if a != b:
            t[int(a)] += 1
    print(max(t))