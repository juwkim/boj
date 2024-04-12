import sys
input = sys.stdin.readline

tri = {}
for _ in range(int(input())):
    K, *l = input().split()
    cur = tri
    for t in l:
        if t not in cur:
            cur[t] = {}
        cur = cur[t]
def solve(cur, depth=0):
    for k, v in sorted(cur.items()):
        print('--' * depth + k)
        solve(v, depth + 1)
solve(tri)