D = int(input())
cnt = [0]
h, m = 12, 1
for _ in range(min(D, 719)):
    if h < 10:
        a, b, c = h, m // 10, m % 10
        p = a - b == b - c
    else:
        a, b, c, d = h // 10, h % 10, m // 10, m % 10
        p = a - b == b - c == c - d
    cnt.append(cnt[-1] + p)
    m += 1
    if m == 60:
        m = 0
        h = (h + 1) % 12
q, r = divmod(D, 720)
print(q * cnt[-1] + cnt[r])