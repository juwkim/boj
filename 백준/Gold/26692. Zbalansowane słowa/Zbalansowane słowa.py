from collections import defaultdict

s = input()
ans = 0
for l in (0, 1, 1), (1, 0, 1), (1, 1, 0), (1, -1, 300000), (1, 300000, -1), (300000, 1, -1), (300000, -300001, 1):
    p = {k: v for k, v in zip("abc", l)}
    dic = defaultdict(int)
    dic[0] = 1
    cur = 0
    for c in s:
        cur += p[c]
        ans += dic[cur]
        dic[cur] += 1
print(ans)