import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, *L = map(int, input().split())
    px = [0] * (N + 1)
    for i in range(N):
        px[i + 1] = px[i] + L[i]
    print(min(px[i] + px[N] - px[i + 1] + min(px[i], px[N] - px[i + 1]) for i in range(N)))