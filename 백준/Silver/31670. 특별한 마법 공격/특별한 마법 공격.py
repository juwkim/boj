N, *R = map(int, open(0).read().split())
a, b = 0, R[0]
for i in range(1, N):
    a, b = b, min(a, b) + R[i]
print(min(a, b))