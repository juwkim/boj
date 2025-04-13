g = lambda: [*map(int, input().split())]

N = int(input())
C = g()
W = g()
density = sorted([*zip(W, C)], key=lambda x: x[0] / x[1])
a, b, idx = 0, sum(C), -1
while idx < N - 1 and a < b:
    idx += 1
    a += density[idx][1]
    b -= density[idx][1]
d = density[idx][0] / density[idx][1]
print(sum(abs(w - d * c) for w, c in zip(W, C)))