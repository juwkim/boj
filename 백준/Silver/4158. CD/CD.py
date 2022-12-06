import sys
input = lambda: sys.stdin.readline().rstrip('\n')

while (s:= input()) != '0 0':
    N, M = map(int, s.split())
    a = set(input() for _ in range(N))
    b = set(input() for _ in range(M))
    print(len(a & b))