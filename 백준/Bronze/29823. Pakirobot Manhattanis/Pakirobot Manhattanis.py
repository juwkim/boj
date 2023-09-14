from collections import Counter

N = int(input())
cnt = Counter(input())
ans = abs(cnt['N'] - cnt['S']) + abs(cnt['W'] - cnt['E'])
print(ans)