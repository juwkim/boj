import sys
input = sys.stdin.readline

N = int(input())
h1, h2 = map(int, input().split())
num1, num2 = h2, h1
for _ in range(N - 1):
    a, b = map(int, input().split())
    num1, num2 = b + max(num1 + abs(a - h1), num2 + abs(a - h2)), a + max(num1 + abs(b - h1), num2 + abs(b - h2))
    h1, h2 = a, b
print(max(num1, num2))