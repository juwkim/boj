T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H:
        floor = N % H
    else:
        floor = H
    print(str(floor) + str(-(N // -H)).zfill(2))