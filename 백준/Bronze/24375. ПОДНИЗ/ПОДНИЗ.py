from collections import*
a=Counter(input())&Counter(input())
for c in map(chr,range(97,123)):print(c*a[c],end='')