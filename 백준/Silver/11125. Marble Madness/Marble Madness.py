for _ in range(int(input())):
    B, W = map(int, input().split())
    if W&1:
        print(0, 1)
    else:
        print(1, 0)