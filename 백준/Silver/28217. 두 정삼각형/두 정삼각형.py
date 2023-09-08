import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
A = [g() for _ in range(N)]
B = [g() for _ in range(N)]

def diff1(A, B):
    num = 0
    for i in range(N):
        num += sum(a^b for a, b in zip(A[i], B[i]))
    return num

def diff2(A, B):
    num = 0
    for i in range(N):
        num += sum(a^b for a, b in zip(A[i], B[i][::-1]))
    return num

ans = min(diff1(A, B), diff2(A, B))
for _ in range(2):
    A = [[A[N - 1 - j][N - 1 - i] for j in range(i + 1)] for i in range(N)]    
    ans = min(ans, diff1(A, B), diff2(A, B))
print(ans)