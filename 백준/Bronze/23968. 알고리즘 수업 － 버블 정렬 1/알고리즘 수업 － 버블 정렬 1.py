g = lambda: [*map(int, input().split())]

def bubble_sort(A):
    global K
    for last in range(N-1, 0, -1):
        for i in range(last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                K -= 1
                if K == 0:
                    print(A[i], A[i+1])
                    return
    print(-1)
    return
    

import sys
input = sys.stdin.readline
N, K = g()
A = g()
bubble_sort(A)