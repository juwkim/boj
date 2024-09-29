N, A, B = map(int, input().split())
a, b = 1, 1
for _ in range(N):
    a, b = a + A, b + B
    if a == b:
        b -= 1
    elif a < b:
        a, b = b, a
print(a, b)