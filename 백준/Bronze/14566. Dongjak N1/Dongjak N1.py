g = lambda: [*map(int, input().split())]

input()
s = sorted(g())
a = [j - i for i, j in zip(s, s[1:])]
print(min(a), a.count(min(a)))