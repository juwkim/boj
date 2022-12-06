a, b = input().split()
s = len(a) * sum(int(i) for i in a)
t = len(b) * sum(int(i) for i in b)
print([0, 1, 2][(s > t) - (s < t)])