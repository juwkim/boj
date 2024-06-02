import sys
input = sys.stdin.readline

s = {(0, 1, 2, 3), (0, 1, 4, 5), (4, 5, 6, 7), (2, 3, 6, 7), (0, 2, 4, 6), (1, 3, 5, 7)}
for _ in range(int(input())):
    l = tuple(sorted(map(int, input().split())))
    print(("NO", "YES")[l in s])