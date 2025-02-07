import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    S = int(input())
    path = {}
    All, HasParent = set(), set()
    for _ in range(S - 1):
        a, b = input().split()
        path[a] = b
        All.add(a); All.add(b)
        HasParent.add(b)
    root = (All - HasParent).pop()
    print(f'Scenario #{tc}:')
    cur = root
    print(cur)
    while cur in path:
        cur = path[cur]
        print(cur)
    print()