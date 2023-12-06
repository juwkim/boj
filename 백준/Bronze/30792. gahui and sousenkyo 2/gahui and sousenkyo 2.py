import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
my = int(input())
rank = sum(num > my for num in g()) + 1
print(rank)