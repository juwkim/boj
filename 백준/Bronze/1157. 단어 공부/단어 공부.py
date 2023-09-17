from collections import Counter

cnt = Counter(input().upper())
l = cnt.most_common()
if len(l) > 1 and l[0][1] == l[1][1]:
    print('?')
else:
    print(l[0][0])