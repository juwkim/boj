import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    A, B = g(), g()
    if any(any(i != j and A[i] == B[j] for j in range(5)) for i in range(5)):
        print("YES")
    else:
        print("NO")