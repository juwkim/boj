import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
p = input()
a, b = int(p[:-1]), p[-1]
if a == 1:
    s = ord(b) - ord('C')
elif a <= 20:
    s = 6 * (int(a) - 2) + 3 + ord(b) - ord('A') + 1
elif b == 'D':
    s = 118
else: # b == 'E'
    s = 119

if s <= n + 1:
    n += 2
else:
    n += 1

if n == 120:
    ans = 'full'
elif n == 118:
    ans = '21D'
elif n == 119:
    ans = '21E'
elif n <= 3:
    ans = '1' + chr(ord('C') + n)
else:
    n -= 4
    ans = str(n // 6 + 2) + chr(ord('A') + n % 6)
print(ans)