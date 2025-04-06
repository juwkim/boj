import sys
input = sys.stdin.readline

p = {}
for _ in range(int(input()) - 1):
    a, b = input().split()
    p[a] = b
def solve(node, target):
    cur = node
    while cur in p:
        cur = p[cur]
        if cur == target:
            return True
    return False
a, b = input().split()
print(+(solve(a, b) or solve(b, a)))