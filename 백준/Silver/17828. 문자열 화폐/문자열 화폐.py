N, X = map(int, input().split())
if N * 26 < X or X < N:
    print("!")
else:
    for i in range(N - 1, -1, -1):
        if X <= i * 26 + 1:
            print("A", end="")
            X -= 1
        else:
            a = X - i * 26
            print(chr(ord("A") + a - 1), end="")
            X -= a