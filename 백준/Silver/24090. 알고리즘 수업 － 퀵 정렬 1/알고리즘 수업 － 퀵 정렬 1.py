import sys
sys.setrecursionlimit(10 ** 5)
g = lambda: [*map(int, input().split())]


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    global K
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            K -= 1
            if K == 0:
                print(A[i], A[j])
                
    if i + 1 != r:
        A[i+1], A[r] = A[r], A[i+1]
        K -= 1
        if K == 0:
            print(A[i+1], A[r])
    return i + 1


N, K = g()
A = g()
quick_sort(A, 0, N-1)
if K > 0:
    print(-1)