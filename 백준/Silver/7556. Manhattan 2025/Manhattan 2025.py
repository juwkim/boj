for tc in range(1, 1 + int(input())):
    u = int(input())
    print(f"Scenario #{tc}:")
    for i in range(-u, u + 1):
        print(f"slice #{i + u + 1}:")
        for j in range(-u, u + 1):
            for k in range(-u, u + 1):
                d = abs(i) + abs(j) + abs(k)
                print('.' if d > u else d, end='')
            print()
    print()