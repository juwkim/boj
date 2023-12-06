g = lambda: [*map(int, input().split())]

cur = 0
for _ in range(int(input())):
    P, C = g()
    cur += abs(cur - P) <= C
print(cur)