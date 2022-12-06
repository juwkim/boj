input()
a = [*map(int, input().split())]
s = a.index(-1)
print(min(a[:s]) + min(a[s+1:]))