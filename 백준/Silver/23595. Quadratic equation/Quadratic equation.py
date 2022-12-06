for _ in range(int(input())):
    Y = int(input())
    if Y == 1 or Y == -1e6:
        print(1, - Y - 1, Y)
    else:
        print(1, 1 - Y, - Y)