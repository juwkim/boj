for _ in range(int(input())):
    N = int(input())
    l = sum(map(int, input().split()))
    x = 1
    while N >= l:
        x += 1
        l <<= 2
    print(x)