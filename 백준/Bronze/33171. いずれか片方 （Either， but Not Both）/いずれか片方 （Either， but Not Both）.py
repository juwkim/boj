N, A, B = map(int, open(0))
print(sum((i % A == 0) ^ (i % B == 0) for i in range(1, N + 1)))