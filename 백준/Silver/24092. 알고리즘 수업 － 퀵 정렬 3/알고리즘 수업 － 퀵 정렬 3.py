import sys
from sys import exit
sys.setrecursionlimit(10 ** 5)
g = lambda: [*map(int, input().split())]


def is_same(x):
    if x in check:
        if A[x] == B[x]:
            check.remove(x)
    elif A[x] != B[x]:
        check.add(x)
    if not check:
        print(1)
        exit(0)


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            if i != j:
                A[i], A[j] = A[j], A[i]
                for num in (i, j):
                    is_same(num)
                
    if i + 1 != r:
        A[i+1], A[r] = A[r], A[i+1]
        for num in (i+1, r):
            is_same(num)

    return i + 1

N = int(input())
A = g()
B = g()
check = set()
for i in range(N):
    if A[i] != B[i]:
        check.add(i)
if not check:
    print(1)
else:
    quick_sort(A, 0, N-1)
    print(0)