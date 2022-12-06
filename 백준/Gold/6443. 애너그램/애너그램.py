import sys
input = lambda: sys.stdin.readline().rstrip('\n')

def solve(msg):
    if len(msg) == l:
        print(msg)
        buf.add(msg)
        return
    
    for i in range(l):
        tmp = msg + s[i]
        if check[i] == 0 and tmp not in buf:
            check[i] = 1
            buf.add(tmp)
            solve(tmp)
            check[i] = 0

for _ in range(int(input())):
    s = sorted(input())
    l = len(s)
    check = [0] * l
    buf = set()
    solve("")