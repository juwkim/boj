import sys
input = lambda: sys.stdin.readline().rstrip()


g = lambda: [*map(int, input().split())]

from sys import exit
def heapify(A, k, n):
    global K
    left, right = 2 * k + 1, 2 * k + 2
    
    if right <= n:
        if A[left] < A[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return

    if A[smaller] < A[k]:
        A[k], A[smaller] = A[smaller], A[k]
        K -= 1
        if K == 0:
            print(*A)
            exit(0)
        heapify(A, smaller, n)

def build_min_heap(A, n):
    for i in range(n//2, 0, -1):
        heapify(A, i-1, n-1)


def heap_sort(A):
    global K
    n = len(A)
    build_min_heap(A, n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        K -= 1
        if K == 0:
            print(*A)
            exit(0)
        heapify(A, 0, i - 1)

N, K = g()
A = g()
heap_sort(A)
print(-1)