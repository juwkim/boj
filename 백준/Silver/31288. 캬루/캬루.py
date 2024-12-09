import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, P = input().split()
    N = int(N)
    if N == 1:
        print(6, 3)
        continue
    P = [*P]
    t = sum(map(int, P)) % 3
    for i in range(int(N)):
        if int(P[i]) - t <= 0:
            minus = t - 3
        else:
            minus = t
        P[i] = chr(ord(P[i]) - minus)
        print("".join(P), 3)
        P[i] = chr(ord(P[i]) + minus)