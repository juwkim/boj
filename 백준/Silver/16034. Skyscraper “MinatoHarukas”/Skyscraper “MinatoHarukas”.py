import sys

while b:=int(sys.stdin.readline()):
    for n in range(int((2*b)**.5), 0, -1):
        a, r = divmod(2 * b + n - n * n, 2 * n)
        if r == 0:
            print(f"{a} {n}")
            break