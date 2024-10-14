import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n = int(input())
a = g()
m = int(input())
b = g()

s = sum(a)
print(sum(num < s for num in b))
for i in range(n):
    if a[i] <= 0:
        print(i + 1, end=' ')
for i in range(n):
    if a[i] > 0:
        print(i + 1, end=' ')