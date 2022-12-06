N, M = map(int, input().split())
A = input()
for _ in range(M):
    S, flag, i = input(), 0, 0
    for alphabet in S:
        if alphabet == A[flag]:
            flag += 1
        if flag == N:
            break
    print('true' if flag == N else 'false')