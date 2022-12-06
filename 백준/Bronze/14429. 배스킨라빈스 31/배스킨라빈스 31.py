g = lambda: [*map(int, input().split())]

N = int(input())
num, min_q = 0, 1e9
for i in range(N):
    j, m = g()
    q = (j - 1) // (m + 1)
    if q < min_q:
        min_q = q
        num = i
print(num + 1, 2 * (min_q + 1))