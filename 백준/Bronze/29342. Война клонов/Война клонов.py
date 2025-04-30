n, *a = map(int, open(0).read().split())
odd = sum(x & 1 for x in a)
even = n - odd
print(odd * even)