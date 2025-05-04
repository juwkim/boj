n, m = map(int, input().split())
cnt_w = [0] * (n + 1)
cnt_e = [0] * (n + 1)
for _ in range(m):
    for i, c in enumerate(input()):
        if c == 'W':
            cnt_w[i + 1] += 1
        else:
            cnt_e[i + 1] += 1
for i in range(n):
    cnt_w[i + 1] += cnt_w[i]
    cnt_e[i + 1] += cnt_e[i]
idx = min((cnt_w[n] - cnt_w[i] + cnt_e[i], i) for i in range(n + 1))[1]
print(idx, idx + 1)