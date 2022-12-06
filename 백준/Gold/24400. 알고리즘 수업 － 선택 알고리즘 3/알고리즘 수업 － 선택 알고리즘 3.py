import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)

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
    global ans
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            for k in [i, j]:
                if k in diff and A[k] == B[k]:
                    diff.remove(k)
                elif k not in diff and A[k] != B[k]:
                    diff.add(k)
            if len(diff) == 0:
                ans = 1
    if i + 1 != r:
        A[i + 1], A[r] = A[r], A[i + 1]
        for k in [i + 1, r]:
            if k in diff and A[k] == B[k]:
                diff.remove(k)
            elif k not in diff and A[k] != B[k]:
                diff.add(k)
        if len(diff) == 0:
            ans = 1

    return i + 1

g = lambda: [*map(int, input().split())]
N, Q = g()
A = g()
B = g()
diff = set(i for i in range(N) if A[i] != B[i])
if len(diff) == 0:
    print(1)
else:
    ans = 0
    select(0, N - 1, Q)
    print(ans)