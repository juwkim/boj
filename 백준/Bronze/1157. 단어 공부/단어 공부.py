from collections import Counter

l = Counter(input().upper()).most_common()
print('?' if len(l) > 1 and l[0][1] == l[1][1] else l[0][0])