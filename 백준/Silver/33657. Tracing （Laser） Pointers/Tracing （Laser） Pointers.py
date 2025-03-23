import sys
input = lambda: sys.stdin.readline().rstrip()

l = []
for _ in range(int(input())):
    *nums, name = input().split()
    x, y, m = map(float, nums)
    if m * y >= 0:
        continue
    l.append((x - y / m, name))
for _, name in sorted(l):
    print(name)