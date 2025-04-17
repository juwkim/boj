g = lambda: [*map(int, input().split())]

N = int(input())
A, B = g(), g()
M = N
for i in range(0, 2 * N, 2):
    s1, e1 = A[i], A[i + 1]
    s2, e2 = B[i], B[i + 1]
    s, e = max(s1, s2), min(e1, e2)
    if s == e:
        M -= 1
    elif s > e:
        M = -1
        break
print(M)