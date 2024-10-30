import sys
input = sys.stdin.readline

a, b = 0, 0
for _ in range(int(input())):
    a, b = b + int(input().split()[2]), max(a, b)
print(max(a, b))