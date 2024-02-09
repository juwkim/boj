g = lambda: map(int, input().split())
N, M = g()
for A, B in sorted(zip(g(), g())):
    if min(M, B) >= A:
        M += B - A
print(M)