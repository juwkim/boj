g = lambda: [*map(int, input().split())]

while (s:= input()) !='0 0':
    buf = [0] * 10
    n, m = map(int, s.split())
    a, b = g(), g()
    
    for i in a:
        for j in b:
            for c in str(i * j):
                buf[int(c)] += 1
    print(*buf)