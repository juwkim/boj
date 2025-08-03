input()
cnt, cur = [1, 0], 0
for x in map(int, input().split()):
    cur ^= x & 1
    cnt[cur] += 1
f0, f1 = cnt
print(f0 * (f0 - 1) + f1 * (f1 - 1) >> 1)