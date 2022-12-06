from collections import Counter
s = Counter(input())
a = sum(s[key]&1 for key in s)
if a == len(s):
    print(1)
elif a == 0:
    print(0)
else:
    print(2)