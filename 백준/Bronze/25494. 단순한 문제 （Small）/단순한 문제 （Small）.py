for _ in range(int(input())):
    a, b, c = map(int, input().split())
    ans = 0
    for x in range(1, 1 + a):
        for y in range(1, 1 + b):
            for z in range(1, 1 + c):
                if x % y == y % z == z % x:
                    ans += 1
    print(ans)