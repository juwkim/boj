import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)
g = lambda: [*map(int, input().split())]
N, Q, K = g()
A = g()
def select(p, r, q):
    if p == r:
        return A[p]
    t = partition(p, r)
    k = t - p + 1
    if q < k:
        return select(p, t - 1, q)
    elif q == k:
        return A[t]
    else:
        return select(t + 1, r, q - k)
    
def partition(p, r):
    global K, flag
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            K -= 1
            if K == 0:
                flag = False
                print(*A)
    if i + 1 != r:
        A[i + 1], A[r] = A[r], A[i + 1]
        K -= 1
        if K == 0:
            flag = False
            print(*A)
    return i + 1

flag = True
select(0, N - 1, Q)
if flag:
    print(-1)