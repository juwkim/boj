import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

input()
print(max(i+num for i, num in enumerate(sorted(g(),reverse=True))))