X, N = map(int, [input(), input()])
print(X * (N + 1) - sum([int(input()) for _ in range(N)]))