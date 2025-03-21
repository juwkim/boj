import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    i = 1
    while a[i] > a[i - 1] or a[i] > a[i + 1]: i += 1
    print(max(sum(a) / n, sum(a[i-1:]) / (n - i + 1), sum(a[:i+2]) / (i + 2)))