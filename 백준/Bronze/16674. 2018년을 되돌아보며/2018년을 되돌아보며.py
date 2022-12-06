s = input()
from collections import Counter
if set(s) - set('2018'):
    print(0)
elif set(s) != set('2018'):
    print(1)
elif len(set(Counter(s).values())) != 1:
    print(2)
else:
    print(8)