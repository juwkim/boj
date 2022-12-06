import sys
input = lambda: sys.stdin.readline().rstrip('\n')

g = lambda: [*map(int, input().split())]

buf = [(h, w) for h in range(1, 150) for w in range(h+1, 151)]
buf.sort(key=lambda x: x[0]**2 + x[1]**2)

dic = {buf[i]: buf[i+1] for i in range(len(buf)-1)}
while (s:= input()) != '0 0':
    h, w = map(int, s.split())
    print(*dic[(h, w)])