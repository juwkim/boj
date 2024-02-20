import sys
input = sys.stdin.readline

while N:=int(input()):
    a, b = 0, 0
    for _ in range(N):
        cmd, m = input().split()
        m = int(m)
        if cmd[0] == 'D':
            b += m
            print(f"DROP 2 {m}")
        elif a >= m:
            a -= m
            print(f"TAKE 1 {m}")
        else:
            if a:
                print(f"TAKE 1 {a}")
            print(f"MOVE 2->1 {b}")
            print(f"TAKE 1 {m - a}")
            a, b = b - (m - a), 0
    print()