from collections import Counter

g = lambda: [*map(int, input().split())]
M, N,  = g()
a = Counter()
for num in map(str, range(M, N+1)):
    a += Counter(num)
print(*[a[i] for i in '0123456789'])