from collections import Counter
for _ in range(int(input())):
    s = input().split()
    a, b = set(Counter(s[1::2]).values()), set(Counter(s[2::2]).values())
    print(['NOT ', ''][a == b == {1}] + 'SAFE')