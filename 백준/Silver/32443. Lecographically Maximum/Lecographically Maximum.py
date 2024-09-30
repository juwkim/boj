N, *a = map(int, open(0).read().split())
cnt = [0] * 32
for num in a:
    for i in range(31):
        if not num:
            break
        cnt[i] += num & 1
        num >>= 1
for _ in range(N):
    num = 0
    for i in range(31):
        if cnt[i]:
            cnt[i] -= 1
            num |= 1 << i
    print(num, end=' ')