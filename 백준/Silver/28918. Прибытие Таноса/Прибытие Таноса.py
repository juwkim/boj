import datetime
from itertools import permutations

ans, check = [], set()
for s in permutations(sorted(input().replace(' ', ''))):
    y, m, d = "".join(s[:4]), "".join(s[4:6]), "".join(s[6:])
    l = " ".join((y, m, d))
    if l in check:
        continue
    try:
        datetime.date(int(y), int(m), int(d))
        ans.append(l)
        check.add(l)
    except:
        pass
print(len(ans))
for l in ans:
    print(l)