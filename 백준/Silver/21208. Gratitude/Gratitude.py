from collections import Counter

N, K = map(int, input().split())
cnt, idx = Counter(), {}
for i in range(3 * N):
    s = input()
    cnt[s] += 1
    idx[s] = i
for k in sorted(cnt.keys(), key=lambda x: (cnt[x], idx[x]), reverse=True)[:K]:
    print(k)