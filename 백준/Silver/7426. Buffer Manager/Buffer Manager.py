N, K = map(int, input().split())
px, i = [0] * (N + 1), 0
for _ in range((N + 79) // 80):
    for c in input():
        if c == '*':
            num = 100000
        else:
            num = int(c)
        px[i + 1] = px[i] + num
        i += 1
idx, num = 0, 9 * K + 1
for i in range(N - K + 1):
    if px[i + K] - px[i] < num:
        idx, num = i + 1, px[i + K] - px[i]
print(idx)