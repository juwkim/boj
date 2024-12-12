g = lambda: map(int, input().split())

N = int(input())
a0, a1, a2 = g()
b0, b1, b2 = g()
d0 = min(N, max(0, 5 - min((a0 - b0) % N, (b0 - a0) % N)))
d1 = min(N, max(0, 5 - min((a1 - b1) % N, (b1 - a1) % N)))
d2 = min(N, max(0, 5 - min((a2 - b2) % N, (b2 - a2) % N)))
print(2 * min(N, 5) ** 3 - d0 * d1 * d2)