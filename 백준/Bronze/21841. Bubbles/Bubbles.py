g = lambda: [*map(int, input().split())]

P, W, N = g()
cnt = [0, 0]
for _ in range(N):
    cnt[input()[0] == 'W'] += 1
print(cnt[0] * P + cnt[1] * W - cnt[0] * cnt[1])