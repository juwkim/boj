a, b = 1, 0
n = int(input())
for _ in range(n):
    a, b = b, a + b
print(b, max(3, n - 2))