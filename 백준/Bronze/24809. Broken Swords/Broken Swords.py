import sys
input = sys.stdin.readline
TB, LR = 0, 0
for _ in range(int(input())):
    a = input()
    TB += a[:2].count('0')
    LR += a[2:].count('0')
s = min(TB, LR) // 2
print(s, TB - 2 * s, LR - 2 * s)