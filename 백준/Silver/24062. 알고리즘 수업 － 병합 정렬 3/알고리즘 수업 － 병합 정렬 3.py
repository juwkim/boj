import sys
input = lambda: sys.stdin.readline().rstrip()

def merge_sort(l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(l, m)
        merge_sort(m+1, r)
        merge(l, m, r)

def merge(l, m, r):
    global ans
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
        if i in diff and A[i] == B[i]:
            diff.remove(i)
        elif i not in diff and A[i] != B[i]:
            diff.add(i)
        if len(diff) == 0:
            ans = 1
            return
        i += 1
        t += 1


g = lambda: [*map(int, input().split())]
N = int(input())
A = g()
B = g()
diff = set(i for i in range(N) if A[i] != B[i])
if len(diff) == 0:
    print(1)
else:
    ans = 0
    merge_sort(0, N - 1)
    print(ans)