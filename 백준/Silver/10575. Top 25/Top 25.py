import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    d = {input(): i for i in range(N)}
    A = [*range(N)]
    B = [d[input()] for _ in range(N)]
    ans = []
    cnt = 0
    a_sum, b_sum = 0, 0
    for a, b in zip(A, B):
        a_sum += a
        b_sum += b
        cnt += 1
        if a_sum == b_sum:
            ans.append(cnt)
            cnt = 0
            a_sum, b_sum = 0, 0
    print(*ans)