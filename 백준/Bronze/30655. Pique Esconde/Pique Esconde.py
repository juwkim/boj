import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

while True:
    n, m = g()
    if n == 0:
        break
    check = set(range(1, n + 1))
    check.remove(m)
    for _ in range(n - 2):
        check.remove(int(input()))
    print(check.pop())