from collections import Counter

input()
cnt = Counter(map(int, input().split()))
num = 1
for _ in range(62):
    if cnt[num] >= 2:
        cnt[num * 2] += cnt[num] // 2
    num <<= 1
print(max(cnt))