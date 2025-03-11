N, a, *A = map(int, open(0).read().split())
b = 0
for num in A: a, b = b + num, max(a, b)
print(max(a, b))