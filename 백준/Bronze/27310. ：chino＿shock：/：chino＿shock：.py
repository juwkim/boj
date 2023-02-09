from collections import Counter

cnt = Counter(input())
print(sum(cnt.values()) + cnt[':'] + cnt['_'] * 5)