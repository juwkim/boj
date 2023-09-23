import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

buf = []
for _ in range(int(input())):
    buf.append(input().split()[1][1:-1])
ans = "".join(buf)
for l in ans.split('\\n'):
    print(l)
