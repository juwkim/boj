import sys
input = lambda: sys.stdin.readline().rstrip()

while n:=int(input()):
    buf = [(input(), input()) for _ in range(n)]
    s = input()
    for k, v in buf:
        while True:
            idx = s.find(k)
            if idx == -1:
                break
            s = s[:idx] + v + s[idx+len(k):]
    print(s)