from collections import Counter
import string

a = Counter(input())
b = Counter(input())
for c in string.ascii_lowercase:
    print(c * max(a[c], b[c]), end="")