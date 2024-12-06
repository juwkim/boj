import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

input()
A = g()
for _ in range(int(input())):
    L, R = g()
    p = L
    for num in A:
        if L <= num <= R:
            print(p, end=' ')
            p += 1
        else:
            print(num, end=' ')
    print()