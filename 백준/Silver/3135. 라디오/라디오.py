g = lambda: [*map(int, input().split())]

A, B = g()
N = int(input())
tmp = min(abs(B - i) for i in [int(input()) for _ in range(N)])
print(min(tmp+1, abs(A-B)))