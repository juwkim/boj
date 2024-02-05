import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    S = [*map(int, input().split())]
    P, A = [0] * N, [0] * N
    for i in range(N + 1 >> 1):
        j = N - i - 1
        if S[i] - S[j] & 1:
            print('NIE')
            break
        num = S[i] + S[j] >> 1
        P[i], P[j] = num, num
        A[i], A[j] = S[i] - num, S[j] - num
    else:
        print(*P)
        print(*A)