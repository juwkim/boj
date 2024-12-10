import sys
input = lambda: sys.stdin.readline().rstrip()

A = [input()[:2*i-1] for i in range(int(input()))]
for _ in range(int(input())):
    b, c = sorted(map(int, input().split()), reverse=True)
    print(A[b][2 * c])