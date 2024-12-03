import sys
input = sys.stdin.readline

def solve():
    P = [-1] * N
    check = set()
    for i in range(N):
        if A[i][i] != 0:
            return -1
        num = 1 + A[i].count(-1)
        if num in check:
            return -1
        check.add(num)
        P[i] = num
    for i in range(N):
        for j in range(N):
            if A[i][j] != +((P[i] < P[j]) - (P[i] > P[j])):
                return -1
    return " ".join(map(str, P))

N = int(input())
A = [[*map(int, input().split())] for _ in range(N)]
print(solve())