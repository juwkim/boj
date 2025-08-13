import sys
input = sys.stdin.readline

n = int(input())
l = [n] * (n + 2)
for _ in range(n):
    a, b = map(int, input().split())
    l[a] -= 1
    l[b] -= 1
print(min(l))