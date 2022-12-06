D, K = map(int, input().split())
s, t = 1, 1
for _ in range(D-3):
    s, t = t, s + t

A = 1
while True:
    B, q = divmod(K - s * A, t)
    if q == 0:
        break
    A += 1
print(A)
print(B)