import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    words = [input() for _ in range(N)]
    A = [input() for _ in range(8)]
    B = ["".join(l) for l in zip(*A)]
    C = ["".join(A[i][i+j] for i in range(8 - j)) for j in range(8)]
    D = ["".join(A[i+j][i] for i in range(8 - j)) for j in range(1, 8)]
    P = A + B + C + D
    if all(any(word in p for p in P) for word in words):
        print("Yes")
    else:
        print("No")