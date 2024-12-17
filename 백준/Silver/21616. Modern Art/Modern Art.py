import sys
input = sys.stdin.readline

M, N, K = int(input()), int(input()), int(input())
row, col = [0] * (M + 1), [0] * (N + 1)
for _ in range(K):
    cmd, num = input().split()
    num = int(num)
    if cmd == 'R':
        row[num] ^= 1
    else:
        col[num] ^= 1
a, b = sum(row), sum(col)
print(a * (N - b) + b * (M - a))