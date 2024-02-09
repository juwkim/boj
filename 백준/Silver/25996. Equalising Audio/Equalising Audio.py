n, x, *a = map(int, open(0).read().split())
t = (n * x / sum(num * num for num in a)) ** .5 if any(a) else 0
print(*[t * num for num in a])