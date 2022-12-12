from collections import Counter
cnt = Counter(input() for _ in range(int(input()))).most_common()
ans, Max = cnt[0]
for i in range(1, len(cnt)):
    if cnt[i][1] == Max:
        ans = max(ans, cnt[i][0])
    else:
        break
print(ans, Max)