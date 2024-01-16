import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

while True:
    s = input()
    idx = s.index('C')
    n, m = int(s[1:idx]), int(s[idx+1:])
    if n == m == 0:
        break
    col = ""
    m -= 1
    while True:
        col = chr(m % 26 + 65) + col
        m //= 26
        m -= 1
        if m == -1:
            break
    print(col + str(n))