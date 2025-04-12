import sys
input = sys.stdin.readline

N = int(input())
a, b, c, d = 0, 0, 0, 0
s = 0, 1, 2, 1
for _ in range(N - 2):
    i = input().index('0')
    a += s[i]
    b += s[i - 1]
    c += s[i - 2]
    d += s[i - 3]
print(min(a, b, c, d) + N + 2)