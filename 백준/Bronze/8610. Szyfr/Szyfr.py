from collections import Counter

n, s = input().split()
p = input()
a = Counter(p).most_common()[0][0]
off = ord(s) - ord(a)
print(*map(lambda x: chr((ord(x) + off - 65) % 26 + 65), p), sep='')