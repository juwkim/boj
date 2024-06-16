N, A, B = map(int, input().split())
print(max(0, (N - 2 * A + 1) * (N - 2 * B + 1) - 1))