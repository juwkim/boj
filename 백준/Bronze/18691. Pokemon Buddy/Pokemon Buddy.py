for _ in range(int(input())):
    G, C, E = map(int, input().split())
    print((2 * G - 1) * max(0, E - C))