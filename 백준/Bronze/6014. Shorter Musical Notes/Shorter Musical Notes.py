import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]

N, Q = g()
arr = []
for i in range(1, 1 + N):
    arr += [i] * int(input())
for _ in range(Q):
    print(arr[int(input())])