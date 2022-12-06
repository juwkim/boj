from collections import Counter
a = Counter(input())
b = Counter(input())
if all(a[k] >= b[k] for k in b):
    print('YES')
else:
    print('NO')