g = lambda: [*map(int, input().split())]

R, C = g()
a, b, c, d = g()
cnt = sum(input().count('P') for _ in range(R))
print(+(cnt < c * d))