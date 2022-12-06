from itertools import permutations
from datetime import date

l = [*map(int, input().split('/'))]
check = set()
for d, m, y in permutations(l, 3):
    try:
        date(2100 + y, m, d)
        ans = '%02d/%02d/%02d' % (d, m, y)
        if ans not in check:
            check.add(ans)
            print(ans)
    except:
        continue
if not check:
    print('No such date')