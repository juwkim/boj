import collections as c
a = c.Counter(open(0).read().replace('\n', '').replace(' ', ''))
b = a.most_common(1)[0][1]
print(''.join(sorted(alpha for alpha in a if b == a[alpha])))