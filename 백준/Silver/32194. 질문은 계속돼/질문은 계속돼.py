import sys
input = sys.stdin.readline

N = int(input())
px = [0] * (N + 2)
px[1] = 1
for i in range(2, N + 2):
    cmd, x, y = map(int, input().split())
    if cmd == 1 and px[y] - px[x - 1] == y - x + 1 or cmd == 2 and px[y] - px[x - 1] == 0:
        print('Yes')
        px[i] = px[i - 1] + 1
    else:
        print('No')
        px[i] = px[i - 1]