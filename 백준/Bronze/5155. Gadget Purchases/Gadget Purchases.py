for i in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    machine = [[*map(int, input().split())] for _ in range(m)]
    check = [0] * m
    for _ in range(n):
        check[int(input()) - 1] += 1
    print(f'Data Set {i}:')
    for j in range(m):
        p, c, u, r = machine[j]
        if (r - c) * min(u, check[j]) > p:
            print(j + 1)
    print()