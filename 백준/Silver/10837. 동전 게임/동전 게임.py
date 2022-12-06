import sys
input = sys.stdin.readline

g = lambda: map(int, input().split())
K = int(input())
for _ in range(int(input())):
    M, N = g()
    remain = K - max(M, N)
    diff = abs(M - N)
    if M == N:
        print(1)
    elif M > N:
        if diff - remain <= 2:
            print(1)
        else:
            print(0)
    else:
        if diff - remain <= 1:
            print(1)
        else:
            print(0)