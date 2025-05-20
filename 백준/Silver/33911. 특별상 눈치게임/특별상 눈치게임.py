cnt = [0] * 101
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1
    cnt[c] += 1
ans = 0
for i in range(1, 99):
    for j in range(i + 1, 100):
        for k in range(j + 1, 101):
            cnt[i] += 1
            cnt[j] += 1
            cnt[k] += 1
            l = [p for p in range(1, 101) if cnt[p] == 1]
            if l and max(l) in (i, j, k):
                ans += 1
            cnt[i] -= 1
            cnt[j] -= 1
            cnt[k] -= 1
print(ans)