from collections import Counter

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
cnt = Counter()
diff = 0
for i in range(N - 1):
    s, t = cnt[a[i]], cnt[b[i]]
    cnt[a[i]] += 1
    cnt[b[i]] -= 1
    if a[i] != b[i]:
        if s == 0:
            diff += 1
        elif s == -1:
            diff -= 1
        if t == 0:
            diff += 1
        elif t == 1:
            diff -= 1
    ans.append(str(b[i]))
    if diff == 0:
        ans.append('#')
ans.append(str(b[-1]))
print(' '.join(ans))