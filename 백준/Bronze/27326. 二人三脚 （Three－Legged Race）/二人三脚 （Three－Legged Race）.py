from collections import Counter

input()
cnt = Counter(input().split())
print(cnt.most_common()[-1][0])