n, k, *pos = map(int, open(0).read().split())
key = [0] * n
for i, p in enumerate(pos): key[p - 1] = i
cycle = key[-1]
for door in range(n):
    cycle += (key[door] - cycle) % n
cycle -= key[-1]

cnt = 0
for door in range((k - 1) % n + 1):
    cnt += (key[door] - cnt) % n
cnt += cycle * ((k - 1) // n)
print(cnt)