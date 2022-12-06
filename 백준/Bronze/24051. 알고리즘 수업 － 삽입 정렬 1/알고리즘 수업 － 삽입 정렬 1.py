g = lambda: [*map(int, input().split())]

def insertion_sort(A):
    global K
    for i in range(1, N):
        loc = i - 1
        newItem = A[i]
        while 0 <= loc and newItem < A[loc]:
            A[loc + 1] = A[loc]
            loc -= 1
            K -= 1
            if K == 0:
                print(A[loc + 1])
                return
        if loc + 1 != i:
            A[loc + 1] = newItem
            K -= 1
            if K == 0:
                print(A[loc + 1])
                return
    print(-1)
    return
    
import sys
input = sys.stdin.readline
N, K = g()
A = g()
insertion_sort(A)