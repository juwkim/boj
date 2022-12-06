N = int(input())
print([(N // 2 + 1)**2, (N // 2 + 1) * (N // 2 + 2)][N % 2])