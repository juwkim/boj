from collections import Counter
input()
s = Counter([i for i in map(int, input().split()) if i]).most_common(2)
print('skipped' if s[0][1] == s[1][1] else s[0][0])