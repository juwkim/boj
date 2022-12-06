from collections import Counter
from functools import reduce
a = Counter('KANGAROO')
b = Counter('KIWIBIRD')
text = input().upper()
kangaroo = reduce(lambda x, y: x+a[y], text, 0)
kiwi = reduce(lambda x, y: x+b[y], text, 0)

print(['Feud continues', 'Kangaroos', 'Kiwis'][(kangaroo > kiwi) - (kangaroo < kiwi)])