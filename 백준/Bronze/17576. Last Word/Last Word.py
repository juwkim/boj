import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]

s = input()
i = 0
for _ in range(int(input())):
    a, b = g()
    i += a
print(s[i:i+b])