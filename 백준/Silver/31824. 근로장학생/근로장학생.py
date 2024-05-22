import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
dic = {}
for _ in range(N):
    Q, A = input().split()
    dic[Q] = A
for _ in range(M):
    ans = []
    S = input()
    for i in range(len(S)):
        tmp = []
        for Q, A in dic.items():
            if S[i:i+len(Q)] == Q:
                tmp.append((Q, A))
        for Q, A in sorted(tmp):
            ans.append(A)
    if ans:
        print(*ans, sep='')
    else:
        print(-1)