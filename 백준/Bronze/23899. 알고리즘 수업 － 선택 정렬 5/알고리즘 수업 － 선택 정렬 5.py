g = lambda: [*map(int, input().split())]

def selection_sort(A):

    for last in range(N-1, 0, -1):
        if A == B:
            print(1)
            return
        
        i = A.index(max(A[:last+1]))
        if last != i:
            A[last], A[i] = A[i], A[last]
    print(1 if A == B else 0)
    return
        
N = int(input())
A = g()
B = g()
selection_sort(A)