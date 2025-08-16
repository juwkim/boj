import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def solve(A):
    if len(A) <= 1:
        return 1
    B, C = [], []
    P = A[len(A) - 1 >> 1]
    for num in A:
        if num < P:
            B.append(num)
        elif num > P:
            C.append(num)
    if B and C:
        return 0
    return solve(B) and solve(C)

for tc in range(1, int(input()) + 1):
    N = int(input())
    A = [*map(int, input().split())]
    print(f"Case #{tc}: {('NO', 'YES')[solve(A)]}")