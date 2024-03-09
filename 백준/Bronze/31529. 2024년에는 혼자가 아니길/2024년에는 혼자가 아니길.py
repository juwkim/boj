X, Y = map(int, input().split())
if X <= Y <= 2 * X:
    print(506 * (2 * X - Y))
else:
    print(-1)