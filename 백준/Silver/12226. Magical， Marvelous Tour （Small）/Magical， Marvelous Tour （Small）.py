import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    N, p, q, r, s = map(int, input().split())
    nums = [(i * p + q) % r + s for i in range(N)]
    px = [0] * (N + 1)
    for i in range(N):
        px[i + 1] = px[i] + nums[i]
    ans = 0
    for i in range(N):
        for j in range(i, N):
            if i == 0:
                num = max(px[j + 1], px[N] - px[j + 1])
            elif j == N - 1:
                num = max(px[i], px[N] - px[i])
            else:
                num = max(px[i], px[j + 1] - px[i], px[N] - px[j + 1])
            ans = max(ans, px[N] - num)
    print(f"Case #{tc}: {ans / px[N]}")