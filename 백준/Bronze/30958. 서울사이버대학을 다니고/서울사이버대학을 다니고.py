from collections import Counter

input()
cnt = Counter(input())
del cnt[' '], cnt['.'], cnt[',']
print(max(cnt.values()))