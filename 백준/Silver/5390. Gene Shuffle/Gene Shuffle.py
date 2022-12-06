g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N = int(input())
    check = set()
    cur = 1
    idx = 1
    for a, b in zip(g(), g()):
        for num in (a, b):
            if num in check:
                check.remove(num)
            else:
                check.add(num)
        if not check:
            print(f'{cur}-{idx}', end=' ')
            cur = idx + 1
        idx += 1
    print()