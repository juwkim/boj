from collections import Counter
s = Counter(input())
for k, v in sorted(s.items(), key=lambda x: (-x[1], x[0])):
    print(k * v, end='')