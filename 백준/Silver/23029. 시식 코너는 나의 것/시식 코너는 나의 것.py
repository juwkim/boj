import sys
input = sys.stdin.readline

a, b, c = 0, 0, 0
for _ in range(int(input())):
    num = int(input())
    a, b, c = max(a, b, c), a + num, b + num // 2
print(max(a, b, c))