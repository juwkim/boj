g = lambda: [*map(int, input().split())]
N, K = g()
A = g()

def merge_sort(l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(l, m)
        merge_sort(m+1, r)
        merge(l, m, r)

def merge(l, m, r):
    global K, ans
    i, j, t = l, m + 1, 0
    tmp = []
    while i <= m and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            t += 1
            i += 1
        else:
            tmp.append(A[j])
            t += 1
            j += 1
    
    while i <= m:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    i, t = l, 0
    while i <= r:
        A[i] = tmp[t]
        K -= 1
        if K == 0:
            ans = A[i]
        i += 1
        t += 1

ans = -1
merge_sort(0, N - 1)
print(ans)