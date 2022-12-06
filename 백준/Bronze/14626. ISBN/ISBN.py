s = input()
a = sum(int(s[i]) * (1 + i % 2 * 2) for i in range(len(s)) if s[i] != '*') % 10
if s.index('*') & 1:
    print(a * 3 % 10)
else:
    print(10 - a if a else 0)