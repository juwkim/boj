import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    L = int(input())
    A = input()
    B = input()
    s = set()
    for i in range(L):
        for j in range(i, L):
            s.add(tuple(sorted(B[i:j + 1])))
    ans = 0
    for i in range(L):
        for j in range(i, L):
            ans += tuple(sorted(A[i:j + 1])) in s
    print(f'Case #{tc}: {ans}')