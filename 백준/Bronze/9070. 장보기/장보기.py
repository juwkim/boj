for _ in range(int(input())):
    g_to_c, good = 0, 0
    for _ in range(int(input())):
        W, C = map(int, input().split())
        if W/C > g_to_c:
            g_to_c = W/C
            good = C
        elif W/C == g_to_c:
            good = min(good, C)
    print(good)