import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

for _ in range(int(input())):
    s = input()
    cnt = Counter([c for c in s if c.isalpha()])
    a, *l = cnt.most_common()
    if l and a[1] == l[0][1]:
        print("NOT POSSIBLE")
    else:
        d = (ord(a[0]) - ord('E')) % 26
        ans = []
        for c in s:
            if c == ' ':
                ans.append(' ')
            else:
                ans.append(chr((ord(c) - d - ord('A')) % 26 + ord('A')))
        print(d, end=' ')
        print(*ans, sep='')