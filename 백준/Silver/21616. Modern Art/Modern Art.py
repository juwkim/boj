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
print(sum(row[i] ^ col[j] for i in range(1, M + 1) for j in range(1, N + 1)))